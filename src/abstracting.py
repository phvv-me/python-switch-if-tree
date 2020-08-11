from abc import ABC, abstractmethod
from enum import Enum
from dataclasses import dataclass
from typing import Hashable, Mapping, Optional
from collections import namedtuple

# the code below won't run

if fruit.kind == "apple":
    result = actions.juice(fruit)
elif fruit.kind == "orange":
    result = actions.cut(fruit)
elif fruit.kind == "banana":
    result = actions.peel(fruit)
else:
    raise ValueError(f"{fruit.kind} is not available")

energy = actions.eat(result)

if fruit.kind == "apple":
    result = evaluate(energy, fruit)
elif fruit.kind == "orange":
    result = evaluate(fruit=fruit)
elif fruit.kind == "banana":
    result = evaluate(energy)
else:
    raise ValueError(f"{fruit.kind} is not available")

process(result)


@dataclass
class BaseFruitModel(ABC):
    fruit: Mapping
    energy: Optional[str] = None

    registry = {}

    def __init_subclass__(cls, /, fruit: Hashable, **kwargs):
        super().__init_subclass__(**kwargs)

        # register the child class as subclassed
        BaseFruitModel.registry[fruit] = cls

    @abstractmethod
    def prepare(self):
        raise NotImplementedError

    @abstractmethod
    def evaluate(self):
        raise NotImplementedError

    def eat(self):
        fruits = self.registry.get(self.fruit).prepare()
        return f"you {fruits}. Delicious!"


class FruitKind(Enum):
    APPLE = "apple"
    ORANGE = "orange"
    BANANA = "banana"


class AppleModel(BaseFruitModel, fruit=FruitKind.APPLE):
    def make_juice(self):
        ...
        return "apple juice"

    def prepare(self):
        return self.make_juice()


class OrangeModel(BaseFruitModel, fruit=FruitKind.ORANGE):
    def pluck(self):
        ...
        return "an orange"

    def cut(self):
        return f"cut {self.pluck()}"

    def prepare(self):
        return self.cut()


class BananaModel(BaseFruitModel, fruit=FruitKind.BANANA):
    def buy(self):
        ...
        return "12 bananas"

    def prepare(self):
        return f"peel {self.buy}"

