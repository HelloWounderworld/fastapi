# From Python3.9+ ins't necessary to import "from typing import List"
def process_item(items: list[str]):
    for item in items:
        print(item)

def process_items(items_t: tuple[int, int, str], items_s: set[bytes]):
    return items_t, items_s

def process_items_dict(prices: dict[str, float]):
    for item_name, item_price in prices.items():
        print(item_name)
        print(item_price)

# From Python3.10 above
def process_item_union(item: int | str):
    print(item)

# For None case
from typing import Optional

def say_hi(name: Optional[str] = None):
    if name is not None:
        print(f'Hey {name}!')
    else:
        print("Hello Wounderworld!")

# Optional is, actually, equivalent with Union
def say_hi_union(name: str | None = None):
    if name is not None:
        print(f"Hey {name}!")
    else:
        print("Hello Wounderwolrd!")

# More shorted

def say_hi_union_short(name: str | None):
    print(f"Hey {name}!")
