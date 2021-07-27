class Product():
    def __init__(self, id, name, price):

        if type(price) != 'float':
            print('Wrong format!')

        self.id = id
        self.name = name
        self.price = price


def main():
    television = Product(10, "32inch", 299.99)
    print(television.id)
    print(television.name)
    print(television.price)


if __name__ == "__main__":
    main()
