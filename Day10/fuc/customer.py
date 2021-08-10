from BIDV import BIDV
from tech import Tech
from payment import Payment

class customer:
    __payment_method =[]
    __current_payment_method = None
    def __init__(self, name):
        self.name=name
    
    def add_payment_method(self, payment):
        self.__payment_method.append(payment)
        
        if self.__current_payment_method == None:
            self.__current_payment_method = payment

    def set_curren_payment_method(self, id):
        self.__current_payment_method = id

    def charge(self, money):
        self.__payment_method[self.__current_payment_method].charge(money)


if __name__ == '__main__':
    Bidv = BIDV('123456789')
    tech = Tech('159357')

    fuc_deeptry = customer('fuc')
    fuc_deeptry.add_payment_method(Bidv)
    fuc_deeptry.add_payment_method(tech)
    fuc_deeptry.set_curren_payment_method(1)
    fuc_deeptry.charge('100000')