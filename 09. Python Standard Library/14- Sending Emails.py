from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from pathlib import Path


message = MIMEMultipart()
message["from"] = "John Doe"
message["to"] = "john@example.com"
message["subject"] = "This is a test"

message.attach(MIMEText("This is a test"))
message.attach(MIMEImage(Path("image.png").read_bytes()))

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()  # identify ourselves to smtp server
    smtp.starttls()  # secure the connection
    # login to our email account
    smtp.login("your_email@gmail.com", "your_password")
    smtp.send_message(message)  # send the message
    smtp.quit()  # close the connection
