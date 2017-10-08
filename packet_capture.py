import pyshark

net_interface = 'wlan0'
capture_time = 30

capture = pyshark.LiveCapture(interface=net_interface)
capture.sniff(timeout=capture_time)

for i in range(len(capture)):
    print(capture[i])