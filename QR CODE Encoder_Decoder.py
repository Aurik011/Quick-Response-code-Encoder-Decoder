#pip install qrcode
#pip install pyzbar
#pip install pillow
import qrcode
#from pyzbar.pyzbar import decode
#from PIL import Image

data = 'Welcome to QRCODE ENCODER DECODER TEST'

img = qrcode.make(data)

img.save('/Users/aurikanjum/PycharmProjects/pythonProject/aurikqrcode.png')
