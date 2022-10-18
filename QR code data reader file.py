from pyzbar.pyzbar import decode
from PIL import Image

img = Image.open('/Users/aurikanjum/PycharmProjects/pythonProject/aurikqrcode.png')

result = decode(img)

print(result)

