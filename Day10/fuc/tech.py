class Tech:
    def __init__(self, phone_number) -> None:
        self.phone_number = phone_number

    def charge(self, money):
        print(f"TechComBank: {money}")