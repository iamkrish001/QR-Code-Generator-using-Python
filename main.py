import pyqrcode 
from pyqrcode import QRCode 
  
# String which represent the QR code 
s = "https://github.com/iamkrish001"   
a = "https://www.krishbhurtel.com.np"
b = "https://www.linkedin.com/in/krish-bhurtel-894946233/"
d = "https://www.instagram.com/b_krishhh/"
# Generate QR code 
url = pyqrcode.create(s) 
url = pyqrcode.create(a) 
url = pyqrcode.create(b) 
url = pyqrcode.create(d) 
  
# Create and save the png file naming "myqr.png" 
url.png("mygithub.png", scale = 5)
url.png("mywebsite.png", scale = 5)
url.png("mylinkedin.png", scale = 5)
url.png("myinstagram.png", scale = 5)