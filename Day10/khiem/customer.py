from tpbank import Tpbank
from bidv import Bidv
from zalopay import Zalopay
class Customer:
    __list_payment_method = []
    __current_payment_method = None

    def __init__(self, name):
        self.name = name

    def add_current_payment(self,method):
        self.__list_payment_method.append(method)

    def set_current_payment_method(self,method_id):
        self.__current_payment_method = self.__list_payment_method[method_id]
        if self.__current_payment_method is None:
            self.__current_payment_method =1
    
    def charge(self, money):
        payment = Zalopay(self.__current_payment_method)
        payment.charge(money)

if __name__ == '__main__':
    custommer = Customer("khiem")
    tpbank = Tpbank("0964161194")
    bidv = Bidv("0964161195")
    custommer.add_current_payment(tpbank)
    custommer.add_current_payment(bidv)
    custommer.set_current_payment_method(1)
    custommer.charge('6000000')