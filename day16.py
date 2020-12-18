from typing import Dict, List

rules: Dict[str, List[int]] = {}
my_ticket: List[int] = []
nearby_tickets: List[List[int]] = []

with open("data/16") as f:
    current_state: str = "RULES"
    for l in f:
        if l == "\n":
            continue
        elif l == "your ticket:\n":
            current_state = "YOUR"
        elif l == "nearby tickets:\n":
            current_state = "NEARBY"
        elif current_state == "RULES":
            rules[l.split(":")[0]] = []
            for rule in l.split(": ")[1].split(" or "):
                rules[l.split(":")[0]].extend(
                    [x for x in range(
                        int(rule.split("-")[0]),
                        int(rule.split("-")[1]) + 1
                    )
                    ])
        elif current_state == "YOUR":
            my_ticket = [int(x) for x in l.strip("\n").split(",")]
        elif current_state == "NEARBY":
            nearby_tickets.append([int(x) for x in l.strip("\n").split(",")])


def invalid_tickets() -> int:
    invalid: int = 0
    for ticket in nearby_tickets:
        for val in ticket:
            valid: bool = False
            for rule in rules:
                if val in rules[rule]:
                    valid = True
                    break
            if not valid:
                invalid += val

    return invalid


def determine_ticket() -> int:

    # Remove Invalid Tickets
    valid_tickets: List[List[int]] = [my_ticket]
    for ticket in nearby_tickets:
        ticket_valid: bool = True
        for val in ticket:
            valid: bool = False
            for rule in rules:
                if val in rules[rule]:
                    valid = True
            if not valid:
                ticket_valid = False
                break
        if ticket_valid:
            valid_tickets.append(ticket)

    # Find Possible Positions for Each Rule
    rule_positions: Dict[str, List[int]] = {}
    for rule in rules:
        for i in range(len(my_ticket)):
            if i in rule_positions.values():
                continue
            position_valid: bool = True
            for ticket in valid_tickets:
                if ticket[i] not in rules[rule]:
                    position_valid = False
                    break
            if position_valid:
                if rule in rule_positions:
                    rule_positions[rule].append(i)
                else:
                    rule_positions[rule] = [i]

    # Filter down to find individual positions
    for _ in range(len(rule_positions)):
        for rule in rule_positions:
            if len(rule_positions[rule]) == 1:
                for r_rule in rule_positions:
                    if rule != r_rule:
                        try:
                            rule_positions[r_rule].remove(
                                rule_positions[rule][0])
                        except:
                            pass

    # Find value
    value: int = 1
    for key in rule_positions:
        if key.startswith("departure"):
            value *= my_ticket[rule_positions[key][0]]

    return value


print(invalid_tickets())
print(determine_ticket())
