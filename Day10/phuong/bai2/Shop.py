# import math

# a = int(input())
# b = int(input())
# c = int(input())

# def alpha(a, b, c):
#     alpha = float(math.acos((a**2 + b**2- c**2)/2*a*b))
#     return alpha

# if a+b >= c or b+c >= a or a+c >= b:
#     if a == b and b == c and c == a:
#         # alpha == 60
#         print("Equilateral triangle")
#     if a == b or a == c or b == c:
#         # alpha != 60
#         print("Isosceles triangle")
#     if a != b and a != c and c != b:
#         print("Scalene triangle")

from database import Dabatase


class Shop:
    def __init__(self, name, list_products):
        self.name = name
        self.list_products = list_products

    def get_name(self):
        return self.name

    def get_info(self):
        print (self.name, self.list_products):
        for item in self.list_products:
            print(f'---------------\nAmount')
            print(f"Amount: {item['amount']}, Product: {item['product'].get_name()},Sold: {item['sold_amount']}")

if __name__ == "__main__":
    db = Dabatase
    list_product_object = []

    