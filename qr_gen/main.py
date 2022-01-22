import qrcode
import image
import os

qr = qrcode.QRCode(
    version=15,
    box_size=10,
    border = 5,
)


user_input_url = input('Welcome to QR Generator, please write a URL with HTTP/S: ')

url = user_input_url

qr.add_data(url)
print(url)

new_url_to_file_name = url.split('.',1)[0].split('//',1)[1]

qr.make(fit=True)

img = qr.make_image(fill="black",back_color = "white")

img.save(f'{new_url_to_file_name}.png')

print('__file__:    ', __file__)

os.system(os.getcwd()+f'{new_url_to_file_name}.png')

