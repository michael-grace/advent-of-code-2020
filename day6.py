# Ensure you add a newline at the end your input file

from typing import List, Set

question_groups: List[List[str]] = []
group_numbers: List[int] = []

with open("data/6") as f:
    temp: List[str] = []
    num_in_group: int = 0
    for l in f:
        if l != "\n":
            for x in l[:-1]:
                temp.append(x)
            num_in_group += 1
        else:
            question_groups.append(temp)
            temp = []
            group_numbers.append(num_in_group)
            num_in_group = 0
    question_groups.append(temp)
    group_numbers.append(num_in_group)

def countYes() -> int:
    count: int = 0
    for group in question_groups:
        count += len(set(group))
    return count

def countEveryoneYes() -> int:
    count: int = 0
    for i in range(len(question_groups)):
        for x in set(question_groups[i]):
            if question_groups[i].count(x) == group_numbers[i]:
                count += 1
    return count

print(countYes())
print(countEveryoneYes())
