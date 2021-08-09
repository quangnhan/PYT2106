from BIDV import BIDV
from tech import Tech

class Payment:
    def __init__(self, payment):
        self.payment = payment

    def pay(self, money):
        self.payment.charge(money)


if __name__ == '__main__':
    BIDV1 = BIDV('7894563213')
    pay1= Payment(BIDV1)
    pay1.pay(123)