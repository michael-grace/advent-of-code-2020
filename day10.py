from copy import copy
from typing import List, Dict


class Adaptor:
    used: bool = False

    def __init__(self, joltage) -> None:
        self.joltage: int = int(joltage)
        self.acceptable: List[int] = list(
            range(self.joltage-3, self.joltage + 1)
        )


adaptors: List[Adaptor] = []

with open("data/10") as f:
    for l in f:
        adaptors.append(Adaptor(l.strip("\n")))

device: int = max([x.joltage for x in adaptors])


def calculate_joltage_difference() -> int:
    current_joltage: int = 0
    usable: List[Adaptor] = []

    one_joltage_difference: int = 0
    three_joltage_difference: int = 1  # 1 for device adaptor

    while current_joltage < device:
        usable = []

        for adap in adaptors:
            if current_joltage in adap.acceptable and not adap.used:
                usable.append(adap)

        usable.sort(key=lambda x: x.joltage)

        for adap in usable:
            difference: int = adap.joltage - current_joltage

            if difference == 1:
                one_joltage_difference += 1
            elif difference == 3:
                three_joltage_difference += 1
            else:
                return -1  # Some problem. RIP

            current_joltage = adap.joltage
            adap.used = True

    return one_joltage_difference * three_joltage_difference


def distinct_ways() -> int:
    cache: Dict[int, int] = {}

    def _recursive_join(joltage: int, adaptors: List[Adaptor]) -> int:
        if joltage in cache:
            return cache[joltage]

        ways: int = 0

        if joltage in range(4):
            ways += 1

        possibilities: List[Adaptor] = [
            x for x in adaptors if x.joltage in range(joltage-3, joltage+1)
        ]
        possibilities.sort(reverse=True, key=lambda x: x.joltage)

        for adap in possibilities:
            new_joltage: int = adap.joltage
            cp_adaptors: List[Adaptor] = list(copy(adaptors))
            cp_adaptors.remove(adap)
            ways += _recursive_join(new_joltage, cp_adaptors)

        cache[joltage] = ways
        return ways

    return _recursive_join(device+3, adaptors)


print(calculate_joltage_difference())
print(distinct_ways())
