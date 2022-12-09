import smtplib
import ssl
from email.message import EmailMessage

email_sender = "spikeespigal@gmail.com"
email_password = "yourpassword"
email_receiver = "spikeespigal@gmail.com"

subject = "I'm a nigerian prince and I need your help. Please don't ignore me!"
body = """
I need your help, please send $2000, and in a few weeks I'll send 40 million dollars in diamonds to you,
Jasilene. Please, this is not a scam. I'm truly a nigerian prince. 

Thanks, 
Prince Nga-ba' TTar
"""

em = EmailMessage()
em["From"] = email_sender
em["To"] = email_receiver
em["Subject"] = subject
em.set_content(body)

context = ssl.create_default_context()

print("Sending Email!")
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
print("Success")