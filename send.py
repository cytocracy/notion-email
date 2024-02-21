import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import notion
from dotenv import load_dotenv
import os
import random

load_dotenv()
email = os.getenv("EMAIL_FROM")
print(email)
password = os.getenv("EMAIL_PW")
print(password)

print()

with open("recipients.txt", "r") as f:
    recip = f.read().splitlines()

with open("to.txt", "r") as f:
    to = f.read().splitlines()

with open("signoffs.txt", "r") as f:
    signoffs = f.read().splitlines()

signoff = random.choice(signoffs)

s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login(email, password)

body = "Here is the rehearsal call for tomorrow!\n\n" + notion.get_call() + "\n" + signoff + ",\nTheo"


message = MIMEMultipart()
message["Subject"] = "Test2"
message['To'] = ', '.join(to)
message["Cc"] = ', '.join(recip)
message["From"] = email

message.attach(MIMEText(body, "plain"))
s.sendmail(email, recip, message.as_string())

s.quit()