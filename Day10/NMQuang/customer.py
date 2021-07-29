from mufg import Mufg
from mizuho import Mizuho
from payment import Payment


class Customer:
    __payment_methods = []
    __current_payment_method = None

    def __init__(self, name):
        self.name = name

    def add_payment_method(self, method):
        self.__payment_methods.append(method)

        if self.__current_payment_method is None:
            self.__current_payment_method = method

    def set_payment_method(self, method_id):
        self.__current_payment_method = self.__payment_methods[method_id]

    def charge(self, amount):
        payment = Payment(self.__current_payment_method)
        payment.charge(amount)


def main():
    mufg = Mufg("0909090909")
    mizuho = Mizuho("0909090908")
    tanaka = Customer('Tanaka')
    tanaka.add_payment_method(mizuho)
    tanaka.add_payment_method(mufg)
    tanaka.set_payment_method(1)
    tanaka.charge(200000)


if __name__ == "__main__":
    main()
