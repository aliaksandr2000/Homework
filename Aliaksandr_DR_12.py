from random import randint
from dataclasses import dataclass

NAMES = ["Alex", "Jhon", "Peter", "Victor", "James", "Oliver"]
NAMES_COUNT = len(NAMES)


@dataclass
class ConsumerAnnotation:
    name: str
    account: float


@dataclass
class HouseAnnotation:
    price: float
    square: float


class House:
    def __init__(self, price: float, square: float) -> None:
        self.price = price
        self.square = square

    def __repr__(self) -> str:
        return f"({self.price}$, {self.square} square)"


class Consumer:
    def __init__(self, name: str, account: float) -> None:
        self.name = name
        self.account = account

    def __repr__(self) -> str:
        return f"{self.name} - {self.account}$"


def generate_house_lst(house_count: int) -> list[HouseAnnotation]:
    house_lst = [House(price=randint(10_000, 250_000), square=randint(25, 200)) for _ in range(house_count)]
    return house_lst


def generate_consumer() -> ConsumerAnnotation:
    consumer = Consumer(name=NAMES[randint(0, NAMES_COUNT - 1)], account=randint(10_000, 250_000))
    return consumer


def get_recommendations(house_lst: list[HouseAnnotation], consumer: ConsumerAnnotation) -> dict[
    ConsumerAnnotation, HouseAnnotation]:
    rec_house = [house for house in house_lst if house.price < consumer.account]
    rec_house.sort(key=lambda x: x.square)
    return {"Consumer": consumer, "Recommendations": rec_house[::-1]}

