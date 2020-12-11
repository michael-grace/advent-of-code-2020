from typing import List

forest: List[List[str]] = []

with open("data/3") as f:
    data = f.readlines()
    
    for l in data:
        forest.append(list(l.strip("\n")))
    
    for i in range(len(data)):
        for l in range(len(data)):
            forest[l] += list(data[l].strip("\n"))


def tobogan(right=3, down=1) -> int:
    column: int  = 0
    trees: int = 0
    for row in range(0, len(forest), down):
        if forest[row][column] == "#":
            trees += 1
        column += right
    return trees

def multipleSlopes() -> int:
    total: int = 1
    total *= tobogan(right=1, down=1)
    total *= tobogan(right=3, down=1)
    total *= tobogan(right=5, down=1)
    total *= tobogan(right=7, down=1)
    total *= tobogan(right=1, down=2)
    return total

print(tobogan())
print(multipleSlopes())