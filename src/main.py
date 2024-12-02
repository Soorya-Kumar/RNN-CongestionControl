import context
from src.networkml import NetworkML
from src.network import Network
import matplotlib.pyplot as plt
from src import savegraphs as sg

#------------------------------------------------------------
#------------------------------------------------------------


high_traffic = 1000
medium_traffic = 500
low_traffic = 150

# if you want to change the number of ticks change the value in hostml file also.
No_of_ticks = 100
#------------------------------------------------------------
#------------------------------------------------------------

window_data_high_no = []
window_data_medium_no = []
window_data_low_no = []

throughput_data_high_no = []
throughput_data_medium_no = []
throughput_data_low_no = []

delay_data_high_no = []
delay_data_medium_no = []
delay_data_low_no = []

netno = Network()
netno.add_host("1",16)
netno.add_host("2",16)
netno.add_host("1",16)
netno.add_host("2",16)
netno.add_host("3",16)
netno.add_host("4",16)
netno.add_host("6",16)
netno.add_host("7",16)

netno.add_router("5",16)

netno.link("1","5")
netno.link("2","5")
netno.link("3","5")
netno.link("4","5")
netno.link("6","5")
netno.link("7","5")

netno.generate_forwarding_table_entries()


def simulate_traffic_no(traffic, window_data, throughput_data, delay_data):
    for i in range(traffic):
        netno.hosts["1"].send_random_packet(netno.hosts["2"])
        netno.hosts["3"].send_random_packet(netno.hosts["4"])
        netno.hosts["6"].send_random_packet(netno.hosts["7"])

    for i in range(No_of_ticks):
        netno.step()
        
        window_data.append([
            netno.hosts["1"].tcp.window_size,
            netno.hosts["3"].tcp.window_size,
            netno.hosts["6"].tcp.window_size
        ])
        
        # Collect throughput and delay data
        throughput_data.append([
            len(netno.hosts["1"].tcp.packets_in_flight)*100,
            len(netno.hosts["3"].tcp.packets_in_flight)*100,
            len(netno.hosts["6"].tcp.packets_in_flight)*100
        ])
        
        delay_data.append([
            netno.hosts["1"].tcp.timeout,
            netno.hosts["3"].tcp.timeout,
            netno.hosts["6"].tcp.timeout
        ])



simulate_traffic_no(high_traffic, window_data_high_no, throughput_data_high_no, delay_data_high_no)
simulate_traffic_no(medium_traffic, window_data_medium_no, throughput_data_medium_no, delay_data_medium_no)
simulate_traffic_no(low_traffic, window_data_low_no, throughput_data_low_no, delay_data_low_no)



#------------------------------------------------------------
#------------------------------------------------------------

net = NetworkML()
net.add_host("1",16)
net.add_host("2",16)
net.add_host("3",16)
net.add_host("4",16)
net.add_host("6",16)
net.add_host("7",16)

net.add_router("5",16)

net.link("1","5")
net.link("2","5")
net.link("3","5")
net.link("4","5")
net.link("6","5")
net.link("7","5")

net.generate_forwarding_table_entries()



# Initialize data storage
window_data_high = []
window_data_medium = []
window_data_low = []

throughput_data_high = []
throughput_data_medium = []
throughput_data_low = []

delay_data_high = []
delay_data_medium = []
delay_data_low = []

# Function to simulate traffic and collect data
def simulate_traffic(traffic, window_data, throughput_data, delay_data):
    for i in range(traffic):
        net.hosts["1"].send_random_packet(net.hosts["2"])
        net.hosts["3"].send_random_packet(net.hosts["4"])
        net.hosts["6"].send_random_packet(net.hosts["7"])

    for i in range(No_of_ticks):
        net.step()
        
        window_data.append([
            net.hosts["1"].tcp.window_size,
            net.hosts["3"].tcp.window_size,
            net.hosts["6"].tcp.window_size
        ])
        
        # Collect throughput and delay data
        throughput_data.append([
            len(net.hosts["1"].tcp.packets_in_flight)*100,
            len(net.hosts["3"].tcp.packets_in_flight)*100,
            len(net.hosts["6"].tcp.packets_in_flight)*100
        ])
        
        delay_data.append([
            net.hosts["1"].tcp.timeout,
            net.hosts["3"].tcp.timeout,
            net.hosts["6"].tcp.timeout
        ])

simulate_traffic(high_traffic, window_data_high, throughput_data_high, delay_data_high)
simulate_traffic(medium_traffic, window_data_medium, throughput_data_medium, delay_data_medium)
simulate_traffic(low_traffic, window_data_low, throughput_data_low, delay_data_low)



#------------------------------------------------------------
#------------------------------------------------------------

print("The graphs are stored in the plots folder")
