class ACB:
    def __init__(self, phone):
        self.phone = phone
    def charge(self,money):
        self.money = money
        print("Charge ACB:{}".format(self.money))