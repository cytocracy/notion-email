import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import notion
from dotenv import load_dotenv
import os

load_dotenv()
email = os.getenv("EMAIL_FROM")
password = os.getenv("EMAIL_PW")

with open("recipients.txt", "r") as f:
    recip = f.read().splitlines()

s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login(email, password)

body = "Here is the rehearsal call for tomorrow!\n\n" + notion.get_call()

message = MIMEMultipart()
message["Subject"] = "Tomorrow's Call"
message["From"] = email
message["To"] = ', '.join(recip)

message.attach(MIMEText(body, "plain"))
s.sendmail(email, email, message.as_string())
s.quit()