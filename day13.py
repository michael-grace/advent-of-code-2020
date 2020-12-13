from functools import reduce
from typing import List

with open("data/13") as f:
    l = f.readlines()
    time_to_leave: int = int(l[0].strip("\n"))
    data: List[str] = l[1].strip("\n").split(",")
    buses: List[int] = [int(x) for x in data if x != "x"]


def find_first_bus() -> int:
    i: int = time_to_leave
    while True:
        for bus in buses:
            if i % bus == 0:
                return (i - time_to_leave) * bus
        i += 1


def find_sequence() -> int:
    # Chinese Remainder Theorem
    def _inv(a: int, b: int) -> int:
        b_0: int = b
        x_0: int = 0
        x_1: int = 1
        if b == 1:
            return 1
        
        while a > 1:
            q: int = a//b
            tmp: int = a
            a = b
            b = tmp % b

            tmp = x_0
            x_0 = x_1 - q * x_0
            x_1 = tmp

        if x_1 < 0:
            x_1 += b_0
        return x_1

    times: List[int] = []
    offsets: List[int] = []

    for bus in range(len(data)):
        if data[bus] == "x":
            pass
        else:
            times.append(int(data[bus]))
            offsets.append(-bus)

    sum: int = 0
    prod: int = reduce(lambda x, y: x*y, times)
    for i in range(len(times)):
        p = prod//times[i]
        sum += offsets[i] * _inv(p, times[i]) * p
    return sum % prod


print(find_first_bus())
print(find_sequence())
