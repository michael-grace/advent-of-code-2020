from typing import List, Set
from copy import copy

instruction_set: List[List[any]] = []

with open("data/8") as f:
    for l in f:
        instruction_set.append([l.split(" ")[0], int(l.split(" ")[1])])


def findLoop() -> int:
    accum: int = 0
    visited: Set[int] = set()
    i: int = 0

    while i not in visited:
        instruction: List[any] = instruction_set[i]
        visited.add(i)
        if instruction[0] == "nop":
            i += 1
        elif instruction[0] == "acc":
            accum += instruction[1]
            i += 1
        elif instruction[0] == "jmp":
            i += instruction[1]

    return accum


def fixLoop() -> int:
    for chg in range(len(instruction_set)):
        accum: int = 0
        i: int = 0
        visited: Set[int] = set()
        completed: bool = True
        while i < len(instruction_set):
            if i in visited:
                completed = False
                break
            instruction: List[any] = copy(instruction_set[i])
            if i == chg:
                if instruction[0] == "nop":
                    instruction[0] = "jmp"
                elif instruction[0] == "jmp":
                    instruction[0] = "nop"
                else:
                    completed = False
                    break
            visited.add(i)
            if instruction[0] == "nop":
                i += 1
            elif instruction[0] == "acc":
                accum += instruction[1]
                i += 1
            elif instruction[0] == "jmp":
                i += instruction[1]
        if completed:
            return accum


print(findLoop())
print(fixLoop())
