from momo import Momo
from ACB import ACB
from payment import Payment
class Custommer:
    __payment_method = []
    __current_payment_method = None
    def __init__(self, name):
        self.name = name
    def add_payment_method(self,payment):
        self.__payment_method.append(payment)
    def set_current_payment_method(self,id):
        self.__current_payment_method = self.__payment_method[id]
    def charge(self, money):
        payment = Payment(self.__current_payment_method)
        payment.charge(money)        

if __name__ == '__main__':
    momo = Momo("2468012310")
    ACB = ACB("0979546852")

    meo = Custommer("meo")
    meo.add_payment_method(ACB)
    meo.add_payment_method(momo)

    meo.set_current_payment_method(0)
    meo.charge("350000")