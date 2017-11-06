import pyshark
from base64 import b64encode as b64
from base64 import b64decode

net_interface = 'wlan0'
capture_time = 20

capture = pyshark.LiveCapture(interface=net_interface)
capture.sniff(timeout=capture_time)

for i in range(len(capture)):
    packet = capture[i]
##    print(packet)

    try:
        if packet.http.request_method == 'POST':
            print("Captured packet number : " + str(i + 1))
            print("Posted URL : ", packet.http.request_full_uri)
            print(packet["urlencoded-form"])
    except:
        pass
