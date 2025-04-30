#first install pyqrcode
#pip install pyqrcode
import pyqrcode
from pyqrcode import QRCode

#string which represent the qr code
s="https://www.khandeshiit.com"

#generate QR code
url=pyqrcode.create(s)

#create & save the png file naming "myqr.png"
url.svg("d:\\myclass.svg",scale=8)