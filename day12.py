from typing import List, Dict, Any

with open("data/12") as f:
    instructions: List[Dict[str, Any]] = [
        {"cmd": l[0], "num": int(l.strip("\n")[1:])} for l in f]


def travelling() -> int:
    direction: int = 90
    position: List[int] = [0, 0]

    for move in instructions:
        if move["cmd"] == "N":
            position[1] += move["num"]

        elif move["cmd"] == "E":
            position[0] += move["num"]

        elif move["cmd"] == "S":
            position[1] -= move["num"]

        elif move["cmd"] == "W":
            position[0] -= move["num"]

        elif move["cmd"] == "L":
            direction -= move["num"]
            direction %= 360

        elif move["cmd"] == "R":
            direction += move["num"]
            direction %= 360

        elif move["cmd"] == "F":
            if direction == 0:
                position[1] += move["num"]

            elif direction == 90:
                position[0] += move["num"]

            elif direction == 180:
                position[1] -= move["num"]

            elif direction == 270:
                position[0] -= move["num"]

            else:
                return -1  # Something did a bad

        else:
            return -1  # Oops :(

    return abs(position[0]) + abs(position[1])


def waypoint() -> int:
    ship_position: List[int] = [0, 0]
    waypoint_rel_pos: List[int] = [10, 1]

    for move in instructions:
        if move["cmd"] == "N":
            waypoint_rel_pos[1] += move["num"]

        elif move["cmd"] == "E":
            waypoint_rel_pos[0] += move["num"]

        elif move["cmd"] == "S":
            waypoint_rel_pos[1] -= move["num"]

        elif move["cmd"] == "W":
            waypoint_rel_pos[0] -= move["num"]

        elif move["cmd"] == "L" or move["cmd"] == "R":
            if move["num"] == 180:
                tmp: List[int] = waypoint_rel_pos.copy()
                waypoint_rel_pos = [-tmp[0], -tmp[1]]
                continue

            elif move["num"] == 360:
                continue

            elif move["num"] == 270:
                move["num"] = 90
                move["cmd"] = "L" if move["cmd"] == "R" else "R"

            if move["cmd"] == "L":
                tmp: List[int] = waypoint_rel_pos.copy()
                waypoint_rel_pos = [-tmp[1], tmp[0]]

            elif move["cmd"] == "R":
                tmp: List[int] = waypoint_rel_pos.copy()
                waypoint_rel_pos = [tmp[1], -tmp[0]]

        elif move["cmd"] == "F":
            for _ in range(move["num"]):
                ship_position[0] += waypoint_rel_pos[0]
                ship_position[1] += waypoint_rel_pos[1]

        else:
            return -1  # Oops :(

    return abs(ship_position[0]) + abs(ship_position[1])


print(travelling())
print(waypoint())
