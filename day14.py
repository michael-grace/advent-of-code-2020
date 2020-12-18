from typing import Any, Dict, List

instructions: List[Dict[str, Any]] = []

with open("data/14") as f:
    for l in f:
        if l[:4] == "mask":
            instructions.append({
                "cmd": "MASK",
                "mask": l.strip("\n").split(" = ")[1]
            })
        elif l[:3] == "mem":
            instructions.append({
                "cmd": "MEM",
                "pos": int(l.split("[")[1].split("]")[0]),
                "val": int(l.strip("\n").split(" = ")[1])
            })


def value_modification() -> int:
    current_mask: str = ""
    memory_store: Dict[int, int] = {}
    for instruction in instructions:
        if instruction["cmd"] == "MASK":
            current_mask = instruction["mask"]
        elif instruction["cmd"] == "MEM":
            num: List[str] = list(
                format(instruction["val"], "b").zfill(len(current_mask)))
            for i in range(len(current_mask)):
                if current_mask[i] == "X":
                    pass
                elif current_mask[i] == "0":
                    num[i] = "0"
                elif current_mask[i] == "1":
                    num[i] = "1"
            memory_store[instruction["pos"]] = int("".join(num), 2)
    total: int = 0
    for val in memory_store.values():
        total += val
    return total


def position_modification() -> int:
    def _generate_from_floating(address: str) -> List[str]:
        addresses: List[str] = []
        l_address = list(address)
        if "X" in l_address:
            changing: int = l_address.index("X")
            for i in ["0", "1"]:
                l_address[changing] = i
                addresses.extend(_generate_from_floating("".join(l_address)))
        else:
            addresses.append(address)
        return addresses

    current_mask: str = ""
    memory_store: Dict[int, int] = {}
    for instruction in instructions:
        if instruction["cmd"] == "MASK":
            current_mask = instruction["mask"]
        elif instruction["cmd"] == "MEM":
            mem_addr: List[str] = list(
                format(instruction["pos"], "b").zfill(len(current_mask))
            )
            for i in range(len(current_mask)):
                if current_mask[i] == "0":
                    pass
                elif current_mask[i] == "1":
                    mem_addr[i] = "1"
                elif current_mask[i] == "X":
                    mem_addr[i] = "X"
            for addr in _generate_from_floating("".join(mem_addr)):
                memory_store[int(addr, 2)] = instruction["val"]
    total: int = 0
    for val in memory_store.values():
        total += val
    return total


print(value_modification())
print(position_modification())
