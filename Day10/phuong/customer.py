from Momo import Momo
from Vietcombank import Vietcombank
from BIDV import BIDV
from Payment import Payment

class Customer:
    __payment_method = []
    __current_payment_method = None

    def __init__(self, name):
        self.name = name

    def add_payment_method(self, payment):
        self.__payment_method.append(payment)

        if self.__current_payment_method is None:
            self.__current_payment_method = payment

    def set_payment_method(self, money):
        payment = Payment(self.__current_payment_method)
        payment.charge(money)

if __name__ == "__main__":
    mm = Momo('2444')
    vietcom = Vietcombank('333311')
    bid = BIDV('33115')

    phuong = Customer('Phuong')
    phuong.add_payment_method(mm)
    phuong.add_payment_method(vietcom)
    phuong.add_payment_method(bid)

    phuong.set_payment_method(1)

    phuong.charge('10000')

