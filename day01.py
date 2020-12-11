from typing import List

entries: List[int] = []

with open("data/1") as f:
    for l in f:
        entries.append(int(l))

def solve2020Two() -> int:
    for i in entries:
        for j in entries:
            if i + j == 2020:
                return i*j

def solve2020Three() -> int:
    for i in entries:
        for j in entries:
            if i+j < 2020:
                for k in entries:
                    if i+j+k == 2020:
                        return i*j*k

print(solve2020Two())
print(solve2020Three())