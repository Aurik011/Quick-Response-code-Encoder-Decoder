import qrcode

data = 'Test data Aurik Anjum Quick Response Code'

x = qrcode.QRCode(version= 1, box_size=5, border= 5)
x.add_data(data)

x.make(fit=True)
img = x.make_image(fill_color = 'red')

img.save('/Users/aurikanjum/PycharmProjects/pythonProject/aurikqrcode.png')
