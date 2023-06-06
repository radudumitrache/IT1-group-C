import network
import urequests

username = ''
password = ''

# Set up the Wi-Fi connection
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect('eduroam', (username, password))


while not wifi.isconnected():
    pass

# Print the IP address assigned to the Pico
print('Connected. IP address:', wifi.ifconfig()[0])



r = urequests.get("http://date.jsontest.com")
print(r.json())