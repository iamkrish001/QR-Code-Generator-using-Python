import pyqrcode 
from pyqrcode import QRCode 
  
# String which represent the QR code 
s = "https://github.com/iamkrish001"   
a = "https://www.krishbhurtel.com.np"
# Generate QR code 
url = pyqrcode.create(s) 
url = pyqrcode.create(a) 
  
# Create and save the png file naming "myqr.png" 
url.png("mygithub.png", scale = 10)
url.png("mywebsite.png", scale = 10)