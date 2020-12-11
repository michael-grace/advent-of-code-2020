from typing import List, Dict

passwords: List[Dict[str, any]] = []

with open("data/2") as f:
    for l in f:
        passwords.append({
            "min": int(l.split("-")[0]),
            "max": int(l.split("-")[1].split(" ")[0]),
            "letter": l.split(" ")[1].split(":")[0],
            "password": l.split(" ")[2].strip("\n")
        })


def acceptablePasswords() -> int:
    acceptable: int = 0

    for i in passwords:
        num_of_occurences: int = i["password"].count(i["letter"])
        if num_of_occurences >= i["min"] and num_of_occurences <= i["max"]:
            acceptable += 1
    
    return acceptable

def letterPositions() -> int:
    acceptable: int = 0

    for i in passwords:
        passes: bool = False
        if i["password"][i["min"]-1] == i["letter"]:
            passes = not passes
        if i["password"][i["max"]-1] == i["letter"]:
            passes = not passes
        if passes:
            acceptable += 1
    
    return acceptable

print(acceptablePasswords())
print(letterPositions())