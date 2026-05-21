#email automation
import random
import math
import smtplib #simple mail transfer protocol library

digits="1234567890"
OTP=""

for i in range(6):
    OTP+=digits[math.floor(random.random()*10)]
otp=OTP+"is otp"
msg=otp

s=smtplib.SMTP("smtp.gmail.com",587)
s.starttls()
s.login("tarunsesetti703@gmail.com","gfks yjba veer lwno")
user="tarunsesetti703@gmail.com"
email=input("enter the you want the send otp")
s.sendmail(user,email,msg)

while True:
    a=input("enter the otp")
    if a==OTP:
        print("correct")
    else:
        print("incoorect")
