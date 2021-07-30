from momo import Momo as M
from vietcombank import Vietcombank as V
class Payment:
    def __init__(self,pay):
        self.pay = pay

    def charge(self, money):
        self.pay.charge(money)


if __name__ == "__main__":
    momo = M("0919147526")
    pay = Payment(momo)
    pay.charge("500000")

    vietcom = V("0909489521")
    pay = Payment(vietcom)
    pay.charge("350000")
