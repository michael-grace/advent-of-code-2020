from typing import List
import string

documents: List[str] = []

with open("data/4") as f:
    temp: str = ""
    for l in f:
        if l != "\n":
            temp = "{0} {1}".format(temp, l.strip("\n"))
        else:
            documents.append(temp)
            temp = ""
    documents.append(temp)

expected_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
letters = ['']

def validDocs() -> int:
    valid: int = 0
    for doc in documents:
        passes: bool = True
        for field in expected_fields:
            if "{0}:".format(field) not in doc:
                passes = False
                break
        if passes:
            valid += 1
    return valid

def validFields() -> int:
    valid: int = 0
    for doc in documents:
        # print(doc)
        passes: bool = True
        for field in expected_fields:
            if "{0}:".format(field) not in doc:
                passes = False
                break
        if passes:
            # BYR
            if len(doc.split("byr:")[1].split(" ")[0]) == 4:
                try:
                    year: int = int(doc.split("byr:")[1].split(" ")[0])
                    if year < 1920 or year > 2002:
                        # print("Invalid BYR Year", year)
                        passes = False
                        continue
                except:
                    # print("Not a int BYR year")
                    passes = False
                    continue
            
            # IYR
            if len(doc.split("iyr:")[1].split(" ")[0]) == 4:
                try:
                    year: int = int(doc.split("iyr:")[1].split(" ")[0])
                    if year < 2010 or year > 2020:
                        # print("Invalid IYR Year", year)
                        passes = False
                        continue
                except:
                    # print("Not a int IYR year")
                    passes = False
                    continue

            # EYR
            if len(doc.split("eyr:")[1].split(" ")[0]) == 4:
                try:
                    year: int = int(doc.split("eyr:")[1].split(" ")[0])
                    if year < 2020 or year > 2030:
                        # print("Not a valid EYR year", year)
                        passes = False
                        continue
                except:
                    # print("Not an int EYR year")
                    passes = False
                    continue
            
            # HGT
            height = doc.split("hgt:")[1].split(" ")[0]
            if height[-2:] == "cm":
                try:
                    num: int = int(height[:-2])
                    if num < 150 or num > 193:
                        # print("Invalid CM Height", num)
                        passes = False
                        continue
                except:
                    # print("CM not an int", height[:-2])
                    passes = False
                    continue
            elif height[-2:] == "in":
                try:
                    num: int = int(height[:-2])
                    if num < 59 or num > 76:
                        # print("Invalid inches height", num)
                        passes = False
                        continue
                except:
                    # print("Inches not an int", height[:-2])
                    passes = False
                    continue
            else:
                # print("No height units", height[-2:])
                passes = False
                continue

            # HCL
            colour: str = doc.split("hcl:")[1].split(" ")[0]
            if colour[0] != "#":
                # print("No HCL #", colour)
                passes = False
                continue
            for c in colour[1:]:
                if c not in list("0123456789") and c not in list(string.ascii_lowercase):
                    # print("Invalid colour code for HCL", colour)
                    passes = False
                    continue
            
            # ECL
            if doc.split("ecl:")[1].split(" ")[0] not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                # print("Invalid ECL")
                passes = False
                continue

            # PID
            pid: str = doc.split("pid:")[1].split(" ")[0]
            if len(pid) != 9:
                # print("PID not right length", len(pid))
                passes = False
                continue
            try:
                int(pid)
            except:
                # print("PID not an int", pid)
                passes = False
                continue

        if passes:
            # print("Valid")
            valid += 1
    return valid


print(validDocs())
print(validFields())