import qrcode

try:

# amount = int(input())

    upiUrl = f'upi://pay?pa=7981225047@ybl&pn=Gorre SaiBhargav Reddy&cu=INR'

    img = qrcode.make(upiUrl)

    img.save('Bhargav phonePe QR.png')

    print('success')

except Exception as e:
    print(e)

# import qrcode

# try:
#     # # Prompt user for input
#     # amount = int(input("Enter the payment amount: "))

#     # Construct UPI URL
#     upiUrl = f'upi://pay?pa=7981225047@ybl&pn=Gorre SaiBhargav Reddy&cu=INR'
    
#     print("Generated UPI URL:", upiUrl)  # Print UPI URL for debugging
    
#     # Generate QR code
#     img = qrcode.make(upiUrl)
    
#     # Save QR code image
#     img.save('Bhargav_phonePe_QR.png')
    
#     print('QR code generated successfully')
    
# except ValueError:
#     print("Invalid input! Please enter a valid integer amount.")
# except Exception as e:
#     print("An error occurred:", e)
