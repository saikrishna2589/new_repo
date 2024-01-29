import smtplib,ssl

def email_send(final_message):
    host = "smtp.gmail.com"
    port = 465
    username = "appemailtest89@gmail.com"
    password = "ajokizibuyfobxze"
    receiver = "appemailtest89@gmail.com"

    context = ssl.create_default_context()
    with smtplib.SMTP("smtp.gmail.com") as server:
        server.starttls() and server.login(user=username, password=password)
        server.sendmail(from_addr=username,
                        to_addrs=receiver,
                        msg=final_message)

