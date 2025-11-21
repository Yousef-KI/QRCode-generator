import qrcode

url = input("Enter the URL to convert:  ").strip()
file_path = "qrcode.png"

qr = qrcode.QRCode()
qr.add_data(url)

img = qr.make_image()
img.save(file_path)

print("the qrcode was generated succesfully! ")