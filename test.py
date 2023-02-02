import smtplib
from email.mime.text import MIMEText


s = smtplib.SMTP('smtp.gmail.com', 587)

s.starttls()

s.login("tparker24@shschools.org", "PA883#sw")

recip = ["tparker24@shschools.org", "t-man13@outlook.com"]

message = MIMEText("Hello, this is a test email")
message["Subject"] = "Test Email"
message["From"] = "tparker24@shschools.org"
message["To"] = ', '.join(recip)

s.sendmail("tparker24@shschools.org", "theop.parker@gmail.com", message.as_string())

s.quit()