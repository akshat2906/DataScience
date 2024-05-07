import random
import maskpass
generate_otp = random.randint(000000,1000000)
username = input("Username: ")
password = maskpass.askpass(prompt="Password: ", mask="*")

print ('Your Username: ,', username)
print ('Your Password: ,', password)

print('Here is your OTP for login',generate_otp)

passw = maskpass.askpass(prompt="Enter the OTP to login: ", mask="*")

if passw == str(generate_otp):
    print("Login Successful!")
else:
    print("OTP not matched!")