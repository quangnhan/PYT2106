from momo import Momo as M
from vietcombank import Vietcombank as V
from payment import Payment
class Customer:
    __paymentMethod = []
    __currentPayment = None

    def __init__(self, name):
        self.name = name

    def addPaymentMethod(self, payment):
        self.__paymentMethod.append(payment)

        if self.__currentPayment == None:
            self.__currentPayment = payment

    def set_currentPayment(self , id):
        self.__currentPayment = self.__paymentMethod[id]

    def charge(self, money):
        payment = Payment(self.__currentPayment)
        payment.charge(money)
    
if __name__ == "__main__":
    momo = M("0919147526")
    vietcom = V("0909489521")
    name = Customer("VIP")
    name.addPaymentMethod(momo)
    name.addPaymentMethod(vietcom)
    name.set_currentPayment(1)
    name.charge("5000000")
