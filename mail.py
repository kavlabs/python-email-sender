import smtplib, ssl

port = 587
smtp_server = "smtp.gmail.com"
sender_email = "youremail@gmail.com"
receiver_email = "receiveremail@gmail.com"
# password = input("Type your password and press enter:")
password = "007kavishkapoor#@"
message = """\
Subject: Hi there

This message is sent from Python."""

context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port, None, 30) as server:
    server.ehlo()
    server.starttls(context=context)
    server.ehlo()
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)