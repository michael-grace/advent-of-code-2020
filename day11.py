from copy import deepcopy
from typing import List, Set, Tuple

with open("data/11") as f:
    seat_structure: List[List[str]] = [list(l.strip("\n")) for l in f]

height: int = len(seat_structure)
width: int = len(seat_structure[0])


def seat_changes(look_for_seat: bool, threshold: int) -> int:
    def _all_change(seat_structure: List[List[str]], look_for_seat: bool, threshold: int) -> int:
        changes: Set[Tuple[int, int]] = set()

        for row in range(height):
            for col in range(width):

                count: int = 0
                for d_row in [-1, 0, 1]:
                    for d_col in [-1, 0, 1]:

                        if d_row == 0 and d_col == 0:
                            continue

                        distance: int = 1
                        while True:
                            if row + (distance*d_row) not in range(height) or col + (distance*d_col) not in range(width):
                                break
                            else:
                                if seat_structure[row+(distance*d_row)][col+(distance*d_col)] == "#":
                                    count += 1
                                    break
                                elif seat_structure[row+(distance*d_row)][col+(distance*d_col)] == ".":
                                    if look_for_seat:
                                        distance += 1
                                    else:
                                        break
                                else:
                                    break

                if seat_structure[row][col] == "L":
                    if count == 0:
                        changes.add((row, col))
                elif seat_structure[row][col] == "#":
                    if count >= threshold:
                        changes.add((row, col))

        if len(changes) == 0:
            occupied: int = 0

            for row in seat_structure:
                occupied += row.count("#")

            return occupied

        else:
            for chg in changes:
                if seat_structure[chg[0]][chg[1]] == "L":
                    seat_structure[chg[0]][chg[1]] = "#"
                elif seat_structure[chg[0]][chg[1]] == "#":
                    seat_structure[chg[0]][chg[1]] = "L"

            return _all_change(seat_structure, look_for_seat, threshold)

    return _all_change(deepcopy(seat_structure), look_for_seat, threshold)


print(seat_changes(False, 4))  # Part One
print(seat_changes(True, 5))  # Part Two
