import qrcode

website_link = input('Enter website link: ')
qr = qrcode.QRCode(version=1, box_size=5, border=5)
qr.add_data(website_link)
qr.make()
img = qr.make_image(fill_color = 'pink', back_color = 'white')
img.save('your_qr.png')