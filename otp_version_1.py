import smtplib
import random
from twilio.rest import Client

#User and Twilio info
account_sid = 'AC2ea157f36fb8a183aee3b01102802d4e'
auth_token = '926faf7428af5fe72c4793b950ab1e4a'
client = Client(account_sid, auth_token)
twilio_num = '+16822248086'

#Function to generate OTP
def generateOtp():
    otp = random.randint(100000, 999999)
    return otp


server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender, password)
server.sendmail(sender, receiver, message)

print("OTP sent on ",receiver)
