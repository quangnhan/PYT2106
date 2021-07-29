from tpbank import Tpbank
from bidv import Bidv
class Zalopay:
    def __init__(self, phone):
        self.phone = phone
    
    def charge(self,money):
        self.phone.charge(money)

if __name__ == '__main__':
    tpbank = Tpbank("46416546")
    bidv = Bidv("5555555")
    zpay = Zalopay(bidv)
    zpay = Zalopay(tpbank)
    
    zpay.charge('1000')