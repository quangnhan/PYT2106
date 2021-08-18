import smtplib, ssl
from server import Server
class Gmail:
        __port = 465  # For SSL
        __smtp_server = "smtp.gmail.com"
        __sender_email = "ngbinhkhiem1611@gmail.com"  # Enter your address
        
        __password = "ygcnmzittesvcdax"
        
        def sendmail(self, receiver_email, message):
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL(self.__smtp_server, self.__port, context=context) as server:
                server.login(self.__sender_email, self.__password)
                print('receiver email', receiver_email)
                server.sendmail(self.__sender_email,receiver_email, message)
        def congratulation(self,name_shop, email):
            message = f"""\
            Subject: Hi {name_shop}

            This message is sent from HR.
            Congratulation to you pass with our Test ."""

            self.sendmail(email, message)

if __name__ == "__main__":
   server = Server()
   shopp = server.get_shopper()

   gmail = Gmail()
   for shop in shopp:
       gmail.congratulation(shop['name_shop'], shop['email'])
    
    # receiver_email = "ngbinhkhiem1611@gmail.com"  # Enter receiver address
    # message = """\
    # Subject: Hi there

    # This message is sent from Python."""

    # gmail = Gmail()
    # gmail.sendmail(receiver_email, message)