# how to make password more secure using environment variables?

#smptlib is used as an email library that create email client session
#ssl library is to make the context secure
import smtplib,ssl

host="smtp.gmail.com"
port=465

username = "appemailtest89@gmail.com"
password = "ajokizibuyfobxze"

receiver="appemailtest89@gmail.com"

message="""\
Subject: Hi!
How are you?
Bye!

"""


context=ssl.create_default_context()


with smtplib.SMTP("smtp.gmail.com") as server:
    server.starttls() and server.login(user=username, password=password)
    server.sendmail(from_addr=username,
                    to_addrs=receiver,
                    msg=message)