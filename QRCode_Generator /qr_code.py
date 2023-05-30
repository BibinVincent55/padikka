import qrcode
print("QR Code Generator", end="\n\n")
img = qrcode.make(input("Enter data to be encoded"))
img.save('qrcode.jpg')
print('QR code saved as qrcode.jpg')
