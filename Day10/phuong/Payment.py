from Vietcombank import Vietcombank
from Momo import Momo


class Payment():
    def __init__(self, payment):
        self.payment = payment

    def charge(self, money):
        self.payment.charge(money)


if __name__ == '__main__':
    momo = Momo("0987654321")
    pay = Payment(momo)
    pay.charge("69000")

    vcb = Vietcombank("0123456789")
    pay = Payment(vcb)
    pay.charge("96000")