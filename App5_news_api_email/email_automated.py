# how to make password more secure using environment variables?

# smptlib is used as an email library that create email client session
# ssl library is to make the context secure
import smtplib, ssl
import os


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "appemailtest89@gmail.com"
    password = os.getenv("PASSWORD")

    receiver = "appemailtest89@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)


"""
import smtplib, ssl
import os


def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    username = "appemailtest89@gmail.com"
    # creating environment variable with os (operating system) library so as to keep password safe

    password = os.getenv("PASSWORD")

    receiver = "appemailtest89@gmail.com"

    context = ssl.create_default_context()
    with smtplib.SMTP("smtp.gmail.com") as server:
        server.starttls() and server.login(user=username, password=password)
        server.sendmail(from_addr=username,
                        to_addrs=receiver,
                        msg=message)
"""
