import smtplib
import random

sender = "shreyuchaudhari309@gmail.com"
password = "uhskphlguwvatfsb"
otp = random.randint(100000, 999999)
message = "Your OTP is " + str(otp)

receiver = input("Enter your mail: ")

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender, password)
server.sendmail(sender, receiver, message)

print("OTP sent on ",receiver)