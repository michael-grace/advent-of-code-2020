from typing import List, Dict

seat_codes: List[Dict[str, any]] = []

with open("data/5") as f:
    for l in f:
        seat: Dict[str, any] = {}
        seat["code"]: str = l.strip("\n")
        seat["row"]: int = int(seat["code"].replace("F", "0").replace("B", "1")[:7], 2)
        seat["column"]: int = int(seat["code"].replace("L", "0").replace("R", "1")[-3:], 2)
        seat["id"]: int = (seat["row"] * 8) + seat["column"]
        seat_codes.append(seat)
        
def highestID():
    seat_ids: List[int] = [x["id"] for x in seat_codes]
    return max(seat_ids)
    
def my_seat():
    seat_ids: List[int] = [x["id"] for x in seat_codes]
    missing_ids: List[int] = []
    for row in range(128):
        for col in range(8):
            if (row * 8) + col not in seat_ids:
                missing_ids.append((row*8)+col)
    for seat in missing_ids:
        if seat+1 in seat_ids and seat-1 in seat_ids:
            return seat



print(highestID())
print(my_seat())