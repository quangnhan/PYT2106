class Bidv:
    def __init__(self, phone):
        self.phone = phone
    
    def charge(self,money):
        print(f'Bidv charge{money} with phone number {self.phone}')