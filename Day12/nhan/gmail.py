import smtplib, ssl
from server import Server

class Gmail:
    __port = 465  # For SSL
    __smtp_server = "smtp.gmail.com"
    __sender_email = "quangnhan145@gmail.com"  # Enter your address
    __password = "pgmwzphlbmkkrkrb"

    def send_email(self, receiver_email, message):
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(self.__smtp_server, self.__port, context=context) as server:
            server.login(self.__sender_email, self.__password)
            server.sendmail(self.__sender_email, receiver_email, message)


if __name__ == "__main__":
    server = Server()
    users = server.get_users()

    gmail = Gmail()
    for user in users:
        gmail.congratuation(user["name"], user["email"])

    # receiver_email = "nhan.vo@menlosecurity.com"  # Enter receiver address
    # message = """\
    # Subject: Hi there

    # This message is sent from Python."""
    # gmail.send_email(receiver_email, message)