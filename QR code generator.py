import qrcode

data = '7981225047@ybl'

img = qrcode.make(data)

# Save the QR code image with the data as the filename
img.save('UpiID.png')

print('UPI ID generated successfully')
