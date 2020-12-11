from typing import List

with open("data/9") as f:
    number_sequence: List[int] = [int(x.strip("\n")) for x in f]


def find_failing() -> int:
    for i in range(25, len(number_sequence)):
        target: int = number_sequence[i]
        components: List[int] = number_sequence[i-25:i]
        found: bool = False
        for j in components:
            for k in components:
                if j+k == target:
                    found = True
                    break
        if not found:
            return target
    return -1  # All passed


def encryption_weakness() -> int:
    failed_num: int = find_failing()
    for i in range(len(number_sequence)):
        for j in range(i+2, len(number_sequence)):
            if sum(number_sequence[i:j]) == failed_num:
                return min(number_sequence[i:j]) + max(number_sequence[i:j])
    return -1  # Couldn't Find Sum


print(find_failing())
print(encryption_weakness())
