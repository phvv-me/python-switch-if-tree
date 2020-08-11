# simple switch

key = "preposition"
default = "..."

switch = {
    "noun": "dog",
    "verb": "to bark",
    "adjective": "big",
    "adverb": "loudly",
    "preposition": "of",
}.get(key, default)

assert switch == "of"

# functional switch


def fibonacci_switch(key):
    def loop(n):
        ...

    def recurrent(n):
        ...

    def memoization(n):
        ...

    # you could refactor this as a loop
    return {
        loop.__name__: loop,
        recurrent.__name__: recurrent,
        memoization.__name__: memoization,
    }.get(key, lambda: NotImplemented)


memoization_fibonacci = fibonacci_switch("memoization")
assert (
    memoization_fibonacci(10) is None
), f"Try implementing the {memoization_fibonacci.__name__} function"


# switch with reduce

switch = {
    "noun": {
        "animal": {"mammal": "rabbit", "reptile": "tortoise"},
        "human": "Napoleon Bonaparte",
    },
    "verb": {
        "witchcraft": {"summon", "enchant", "dispel"},
        "sports": {
            "basketball": 5,
            "soccer": 11,
            "volleyball": 7,
            "sumo": 2,
            "darts": 1,
        },
    },
    "adjective": {
        "good": {"excellent": 10, "very good": 8, "okay": 6},
        "bad": {"unbearable": 0, "terrible": 2, "awful": 4,},
    },
    "adverb": ...,
}

path = ("verb", "sports", "sumo")
default = "not found"

item = switch
for key in path:
    try:
        item = item.get(key, default)
    except AttributeError:
        break  # isinstance(item, dict) is False

assert item == 2

from functools import reduce

result = reduce(lambda item, key: item.get(key, default), path, switch)

assert result == item
