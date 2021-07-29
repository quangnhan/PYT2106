class Tpbank:
    def __init__(self, phone):
        self.phone = phone
    
    def charge(self,money):
        print(f'TP bank charge {money} with phone number {self.phone}')