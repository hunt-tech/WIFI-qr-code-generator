#Wifi QR
import wifi_qrcode_generator
ssid = 'Your WIFI name'
type = 'WPA'
password = 'your password'
img = wifi_qrcode_generator.wifi_qrcode(ssid, False, type , password)
img.save(ssid+'.png')