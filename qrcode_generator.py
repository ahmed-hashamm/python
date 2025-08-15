import qrcode
url = input("Enter your url for thr QR Code: ").lower().strip()
image_name = input("Enter the image name you want: ").lower().strip()
qr = qrcode.QRCode(
    box_size=10,
    border=4,
)
qr.add_data(url)
img = qr.make_image(fill_color="red", back_color="black")
img.save(image_name)
print(f"Your QR Code is saved as {image_name}")