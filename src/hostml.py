import pickle
import os
import math
import random
import numpy as np
import wnd_chng_algo as wnd_chng_algo
from models.git.graphs import PyCache as pg
from sklearn.preprocessing import PolynomialFeatures
from collections import deque
import context
from models.device import Device, Device_Type
from models.packet import Packet, Packet_Type

No_of_ticks = 100

class TCPML():
    def __init__(self):
        self.packets_to_send = list()
        self.packets_in_flight = list()
        self.pckts_to_resend = list()
        self.window_size = 1
        self.timeout = 10
        self.ack_recv_flag = False
        self.ack_timeout_flag = False
        self.send_times = {} #dictionary to track send times

class HostML(Device):
    def __init__(self, ip:str, buffer_cap=5):
        super().__init__(ip)
        self.connected_router = None
        self.outgoing_buffer = list()
        self.incoming_buffer = list()
        self.buffer_cap = buffer_cap
        self.tcp = TCPML()
        self.def_seg_no = 1
        pg.plotGraphs(No_of_ticks)
        self.poly_features = PolynomialFeatures(degree=2,interaction_only=True)
        self.throughput_deque = deque(maxlen=50)  # Deque to store throughput values
        self.delay_deque = deque(maxlen=50)  # Deque to store delay values
    
    def link(self, other:Device):
        self.connected_router = other
    
    def get_connected_router(self):
        return self.connected_router
    
    def device_type(self):
        return Device_Type.HOST
    
    def send_pckt(self, pckt: Packet):
        self.tcp.packets_to_send.append(pckt)
        self.tcp.send_times[pckt.get_seg_no()] = self.clock  # Record send time 
    
    def send_random_packet(self, to_device:Device):
        pckt = Packet(self.def_seg_no, self, to_device, Packet_Type.DATA)
        self.send_pckt(pckt)
        self.def_seg_no = self.def_seg_no + 1
    
    def receive_pckt(self, pckt: Packet):
        if len(self.incoming_buffer) < self.buffer_cap:
            self.incoming_buffer.append(pckt)
            if pckt.get_pckt_type() == Packet_Type.ACK:
                seg_no = pckt.get_seg_no()
                if seg_no in self.tcp.send_times:
                    send_time = self.tcp.send_times.pop(seg_no)
                    delay = self.clock - send_time
                    self.tcp.timeout = delay  # Update timeout with actual delay
                    
    def __str__(self):
        msg = "Host IP: {}\r\n".format(self.ip)
        msg = msg + "Connected to {}\r\n".format(self.connected_router.get_ip())
        return msg
    
    def step(self):
        super().step()
        self.tcp.ack_recv_flag = False
        self.tcp.ack_timeout_flag = False
        # handle incoming packets
        for pckt in self.incoming_buffer:
            if pckt.get_pckt_type() == Packet_Type.DATA:
                # send ack packet
                ack_pack = Packet(pckt.get_seg_no(), pckt.get_to(), pckt.get_from(), Packet_Type.ACK)
                self.outgoing_buffer.append(ack_pack)
                pass
            
            elif pckt.get_pckt_type() == Packet_Type.ACK:
                # remove packet from packets in flight and packets to send
                seg_no = pckt.get_seg_no()
                
                index = -1
                for i in range(len(self.tcp.packets_in_flight)):
                    pckt2 = self.tcp.packets_in_flight[i][0]
                    if pckt2.get_seg_no() == seg_no:
                        index = i
                        break
                
                if index >= 0:
                    self.tcp.timeout = self.clock - self.tcp.packets_in_flight[i][1]  # set tcp timeout adaptively
                    self.tcp.packets_in_flight.pop(index)
                
                index = -1
                for i in range(len(self.tcp.packets_to_send)):
                    pckt2 = self.tcp.packets_to_send[i]
                    if pckt2.get_seg_no() == seg_no:
                        index = i
                        break
                
                if index >= 0:
                    self.tcp.packets_to_send.pop(index)
                
                self.tcp.ack_recv_flag = True
                pass
        self.incoming_buffer.clear()
        # resend any timed out packets
        for i in range(len(self.tcp.packets_in_flight)):
            pckt, t = self.tcp.packets_in_flight[i]
            if self.clock - t > self.tcp.timeout:
                self.tcp.pckts_to_resend.append(i)
        
        for i in self.tcp.pckts_to_resend:
            pckt = self.tcp.packets_in_flight[i][0]
            self.tcp.packets_to_send.insert(0, pckt)
            pass
        
        for i in sorted(self.tcp.pckts_to_resend, reverse=True):
            del self.tcp.packets_in_flight[i]
        
        if len(self.tcp.pckts_to_resend) > 0:
            self.tcp.ack_timeout_flag = True
        
        # Calculate throughput
        throughput = len(self.tcp.packets_in_flight)*100 if self.tcp.timeout > 0 else 0
        self.throughput_deque = deque([0] * 50, maxlen=50) 
        self.delay_deque = deque([0] * 50, maxlen=50)
        
        # Calculate delay
        delay = self.tcp.timeout  
        self.delay_deque.append(delay)
        self.throughput_deque.append(throughput)
        
        throughput_array = np.array(self.throughput_deque)   
        output = wnd_chng_algo.model_calling(throughput_array)
        
        ## the output fromm the algo in the range of -1 to 1.
        # To scale it to the range of 0 to 1
        output = (output+1) / 2
        

        if(output < 0.7) :
            new_cnwd = self.tcp.window_size * 0.5
        elif(output > 0.9) :
            new_cnwd = self.tcp.window_size * 1.2
        else :
            new_cnwd = self.tcp.window_size * 0.9
        self.tcp.window_size = int(new_cnwd)
        
        
        
        self.tcp.pckts_to_resend.clear()
        if self.tcp.window_size < 1:
            self.tcp.window_size = 1  # minimum window size
        # send packets
        # send packets only if there are no packets in flight
        if len(self.tcp.packets_in_flight) == 0:

            for i in range(self.tcp.window_size):
                if len(self.tcp.packets_to_send) == 0:
                    break

                pckt = self.tcp.packets_to_send.pop(0)
                self.outgoing_buffer.append(pckt)
                self.tcp.packets_in_flight.append((pckt,self.clock))

            for pckt in self.outgoing_buffer:
                if pckt.get_pckt_type() == Packet_Type.DATA:
                    # print("Host {} sent packet {} to host {}.".format(self.get_ip(), pckt.get_seg_no(), pckt.get_to().get_ip()))
                    pass
                self.connected_router.receive_pckt(pckt)
            
            self.outgoing_buffer.clear()


if __name__ == "__main__":
    h = HostML("1")
    h.step()