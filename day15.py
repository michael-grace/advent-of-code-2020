from typing import Dict, List

with open("data/15") as f:
    g_sequence: List[int] = [int(x) for x in f.read().strip("\n").split(",")]


def num_in_sequence(num: int) -> int:
    sequence: List[int] = g_sequence.copy()
    recent_num_pos: Dict[int, int] = {}
    for i in range(num-1):

        if len(sequence)-1 > i:
            recent_num_pos[sequence[i]] = i
            continue

        if sequence[i] not in recent_num_pos:
            sequence.append(0)
        else:
            sequence.append(i - recent_num_pos[sequence[i]])

        recent_num_pos[sequence[i]] = i

    return sequence[-1]


print(num_in_sequence(2020))
print(num_in_sequence(30000000))
