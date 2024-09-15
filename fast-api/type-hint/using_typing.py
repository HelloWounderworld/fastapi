# From Python3.9+ ins't necessary to import "from typing import List"
def process_item(items: list[str]):
    for item in items:
        print(item)

process_item(['leonardo', 'takashi', 'teramatsu'])
print()

def process_items(items_t: tuple[int, int, str], items_s: set[bytes]):
    return items_t, items_s

text = "Hello Wounderwolrd!"
print(process_items((27, 180, 'idade e altura'), set(text.encode('utf-8'))))
print()

def process_items_dict(prices: dict[str, float]):
    for item_name, item_price in prices.items():
        print(item_name)
        print(item_price)

process_items_dict({'pepino': 1.00, 'linguica': 3.00, 'pirarucu': 30.00, 'pacu assado': 40.25})
print()

# From Python3.10 above
def process_item_union(item: int | str):
    print(item)

process_item_union('Leonardo')
process_item_union(27)
print()

# For None case
from typing import Optional

def say_hi(name: Optional[str] = None):
    if name is not None:
        print(f'Hey, {name}!')
    else:
        print("Hello Wounderworld!")

say_hi()
say_hi('Leonardo')
print()

# Optional is, actually, equivalent with Union
def say_hi_union(name: str | None = None):
    if name is not None:
        print(f"Hey, {name}!")
    else:
        print("Hello Wounderwolrd!")

say_hi_union()
say_hi_union('Leonardo')
print()

# More shorted - Caso curioso
def say_hi_union_short(name: str | None):
    print(f"Hey, {name}!")

say_hi_union_short(None)
say_hi_union_short('Leonardo')
