import pyqrcode 
from pyqrcode import QRCode 
  
# String which represent the QR code 
s = "https://github.com/iamkrish001"   
# Generate QR code 
url = pyqrcode.create(s) 
  
# Create and save the png file naming "myqr.png" 
url.png("mygithub.png", scale = 12)