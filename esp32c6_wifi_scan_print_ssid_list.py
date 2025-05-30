import machine
import network

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
net_list = wlan.scan()
net_list.sort(key=lambda x: -x[3])
use_real_ssid_name = True
for net in net_list:
    ssid_name = net[0].decode('ascii')
    if ssid_name:
        if (use_real_ssid_name):
             print("SSID: {:18s}, strength: {:d}".format(ssid_name,net[3]))
        else:
            print("{:d}".format(net[3]))
