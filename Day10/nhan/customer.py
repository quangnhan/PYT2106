from momo import Momo
from vietcombank import Vietcombank
from payment import Payment

class Customer:
    __payment_method = []
    __current_payment_method = None

    def __init__(self, name):
        self.name = name

    def add_payment_method(self, payment):
        self.__payment_method.append(payment)

        if self.__current_payment_method == None:
            self.__current_payment_method = payment

    def set_current_payment_method(self, id):
        self.__current_payment_method = self.__payment_method[id]

    def charge(self, money):
        payment = Payment(self.__current_payment_method)
        payment.charge(money)

if __name__ == "__main__":
    momo = Momo("123456")
    vietcombank = Vietcombank("123456")

    nhan = Customer("Nhan")
    nhan.add_payment_method(momo)
    nhan.add_payment_method(vietcombank)

    nhan.set_current_payment_method(1)

    nhan.charge("100000")