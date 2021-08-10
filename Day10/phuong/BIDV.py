class BIDV():
    def __init__(self, mail):
        self.email = mail

    def charge(self, money):
        print(f'BIDV charge {money}')

    def get_mail(self, mail):
        print('Registed email: {mail}')
