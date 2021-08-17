import smtplib, ssl


class Mail:
    __port = 465  # For SSL
    __smtp_server = "smtp.gmail.com"
    __sender_email = "quangnhan145@gmail.com"  # Enter your address
    __password = "pgmwzphlbmkkrkrb"


    def send_mail(self, receiver_email):
        message = """\
        Subject: Hi there

        This message is sent from Python."""

        receiver_email = "nhan.vo@menlosecurity.com"  # Enter receiver address
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(self.__smtp_server, self.__port, context=context) as server:
            server.login(self.__sender_email, self.__password)
            server.sendmail(self.__sender_email, receiver_email, message)
