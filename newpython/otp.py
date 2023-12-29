otp = input("Enter the OTP: ")
myotp = otp.find("S-")
print(otp[myotp+2:myotp+7])

