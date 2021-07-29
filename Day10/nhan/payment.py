from momo import Momo
from vietcombank import Vietcombank

class Payment:
    def __init__(self, payment):
        self.payment = payment

    def charge(self, money):
        self.payment.charge(money)

if __name__ == "__main__":
    momo = Momo("123456")
    vietcombank = Vietcombank("123456")

    payment = Payment(vietcombank)
    payment.charge("100000")
    

