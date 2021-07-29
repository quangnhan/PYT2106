# from animal import Animal
# class Dog(Animal):
#     def __init__(self, name, weight, height,color, kind):
#         super().__init__(name, weight, height)
#         self.color = color
#         self.kind = kind
#     def get_name(self):
#         return self._name
#     def set_name(self, name):
#         self._name = name
#     def set_weight(self, weight):
#         self._weight = weight
#     def show(self):
#         # print(f"This is {self._name} with weight={self._weight} and height={self._height}")
#         print("This is {} with weight {} and height {} màu lông: {}  Giống: {}".format(self._name,self._weight, self._height,self.color, self.kind))
# if __name__ == '__main__':
#     dog = Dog("meo", 30, 50, "đỏ", "becge")
#     dog.show()

from momo import Momo
from ACB import ACB
class Payment:
    def __init__(self, payment):
        self.payment = payment
    def charge(self, money):
        self.payment.charge(money)

if __name__ == '__main__':
    momo = Momo("12345678")
    pay = Payment(momo)
    pay.charge("10000")

    ACB = ACB("097854652")
    pay = Payment(ACB)
    pay.charge("35000")

