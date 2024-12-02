import pandas as pd
df = pd.read_csv(r'dataset_and_preprocess/tcp_throughput_data.csv', on_bad_lines='skip')
df = df.dropna(subset=['tcp.len'])
df = df[df['tcp.len'] > 0]
df.drop(['frame.number', 'frame.time_relative', 'ip.src', 'ip.dst', 'ip.proto', 'tcp.srcport', 'tcp.dstport', 'tcp.seq', 'tcp.ack', 'tcp.len', 'tcp.window_size_value', 'tcp.flags', 'tcp.analysis.retransmission', 'time_diff'], axis=1, inplace=True)
df['time_diff'] = df['frame.time_relative'].diff()
df['throughput_bps'] = (df['tcp.len'] * 8) / df['time_diff']

df.to_csv('fdata_throughtput', index=False)