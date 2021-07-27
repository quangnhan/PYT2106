from database import Dabatase


class Product():
    def __init__(self, id, name, price):

        if type(price) != 'float' or type(id) != 'int':
            print('Wrong format!')

        self.id = id
        self.name = str(name)
        self.price = price


def main():
    db = Dabatase()
    television = Product(10, "32inch", 299.99)
    print(television.id)
    print(television.name)
    print(television.price)

    list_products_object = []
    for product in db.list_products:
        obj = Product(product['id'], product['name'], product['price'])
        list_products_object.append(obj)

    for product in list_products_object:
        print(product.name)


if __name__ == "__main__":
    main()
