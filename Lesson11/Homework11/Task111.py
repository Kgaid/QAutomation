class Human:
    default_name: str = 'Unknown'
    default_age: int = 30

    def __init__(self, name: str = default_name, age: int = default_age):
        self.name = name
        self.age = age
        self.__money = 0
        self.__house = None

    @staticmethod
    def default_info():
        return Human.default_name, Human.default_age

    def __make_deal(self, house, price):
        if self.__money >= price:
            self.__money -= price
            self.__house: Human = house
            print("You have bought a house!")
        else:
            print("You have no enough money for this. You need to earn")

    def earn_money(self, accumulation):
        self.__money += accumulation

    def buy_house(self, house, discount):
        last_price = house.final_price(discount)
        self.__make_deal(house, last_price)

    def info(self):
        print(f"The name is {self.name}")
        print(f"The age is {self.age}")
        print(f"Amount of money: {self.__money}")
        print(f"House: {self.__house}")


class House:

    def __init__(self, area: int, price: int):
        self._area = area
        self._price = price

    def final_price(self, discount: int):
        return self._price - discount


class SmallHouse(House):
    def __init__(self):
        super().__init__(area=40, price=100000)


alice = Human(name="Alice", age=38)
alice.info()
apartment = SmallHouse()
alice.buy_house(apartment, discount=10000)
alice.earn_money(99000)
alice.buy_house(apartment, discount=5000)
