import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import notion
from dotenv import load_dotenv
import os
import random

load_dotenv()
email = os.getenv("EMAIL_FROM")
# print(email)
password = os.getenv("EMAIL_PW")
# print(password)

print()

with open("/home/theop/notion-email/recipients.txt", "r") as f:
    recip = f.read().splitlines()

with open("/home/theop/notion-email/to.txt", "r") as f:
    to = f.read().splitlines()

with open("/home/theop/notion-email/signoffs.txt", "r") as f:
    signoffs = f.read().splitlines()

signoff = random.choice(signoffs)

s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login(email, password)

call = notion.get_call()
# call_list = call.splitlines()

body = "Here is the rehearsal call for tomorrow!<br><br>" +  '<font face="Courier New, Courier, monospace">' + notion.get_call().replace("\n", "<br>") + "</font>"
link = MIMEText("<br><b>Week at a Glance: " + '<a href="https://theoparker.notion.site/6e08eaffba374dd9a1786c66ca3845fb?v=45a78417f24e4681851c7ed282836123&pvs=4">here</a></b>', 'html') 
sign = "\n\n" + signoff + ",\nTheo"

message = MIMEMultipart()
message["Subject"] = "Tomorrow's Rehearsal Call"
message['To'] = ', '.join(to)
message["Cc"] = ', '.join(recip)
message["From"] = email

message.attach(MIMEText(body, "html"))
message.attach(link)
message.attach(MIMEText(sign, "plain"))
s.sendmail(email, recip, message.as_string())

s.quit()