from zalopay import Zalopay
from tpbank import Tpbank
from bidv import Bidv
class Customer:
    __payment_method = []
    __current_payment = None

    def __init__(self, name):
        self.name = name

    def add_payment_method(self, method):
        self.__payment_method.append(method)

    def set_payment_method(self,payment_method_id):
        self.__current_payment = self.__payment_method[payment_method_id]
        if self.__current_payment != None:
            self.__current_payment == 1

    def charge(self,money):
        payment = Zalopay(self.__current_payment)
        payment.charge(money)

if __name__ == "__main__":
    customers = Customer('Khiem')
    tpbank = Tpbank('0123456')
    bidv = Bidv('0654321')
    customers.add_payment_method(tpbank)
    customers.add_payment_method(bidv)
    customers.set_payment_method(1)
    customers.charge('2000')
    