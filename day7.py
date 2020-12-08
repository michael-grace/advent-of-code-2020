from typing import Dict, List

bag_rules: Dict[str, List[str]] = {}
bag_results: Dict[str, bool] = {}

with open("data/7") as f:
    for l in f:
        key: str = l.split(" bags contain ")[0]
        bag_info: List[str] = l.split(" bags contain ")[1].split(", ")
        vals: List[str] = []
        for contained_bag in bag_info:
            count: int
            if contained_bag.split(" ")[0] == "no":
                count = 0
            else:
                count = int(contained_bag.split(" ")[0])
            for i in range(count):
                vals.append(" ".join(contained_bag.split(" ")[1:-1]))
        bag_rules[key] = vals
        bag_results[key] = None


def goldBags() -> int:
    def _canContainGold(bag: str) -> bool:
        if bag == "shiny gold":
            return True
        else:
            for contains in bag_rules[bag]:
                result: any = bag_results[contains]  # Bool or None
                if result:
                    return True
                elif result is None:
                    if _canContainGold(contains):
                        bag_results[contains] = True
                        return True
                    else:
                        bag_results[contains] = False
        return False

    count: int = 0
    for bag in bag_rules:
        if _canContainGold(bag):
            count += 1
            bag_results[bag] = True
        else:
            bag_results[bag] = False
    return count - 1  # Minus one because shiny gold bag isn't holding itself


def countBags() -> int:
    def _countInnerBags(bag: str) -> int:
        count: int = 0
        for contains in bag_rules[bag]:
            count += 1
            count += _countInnerBags(contains)
        return count

    return _countInnerBags("shiny gold")


print(goldBags())
print(countBags())
