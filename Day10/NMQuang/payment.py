from mufg import Mufg
from mizuho import Mizuho


class Payment:
    def __init__(self, payment):
        self.payment = payment

    def charge(self, money):
        self.payment.charge(money)


def main():
    mufg = Mufg('0909090909')
    payMufg = Payment(mufg)
    payMufg .charge(200000)

    mizuho = Mizuho('0909090908')
    payMizuho = Payment(mizuho)
    payMizuho .charge(300000)


if __name__ == "__main__":
    main()
