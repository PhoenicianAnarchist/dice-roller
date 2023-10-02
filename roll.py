#!/usr/bin/env python3
import argparse
import random
import re

parser = argparse.ArgumentParser()
parser.add_argument("-r", "--roll", default="1d6")
parser.add_argument("-d", "--detailed", action="store_true")
args = parser.parse_args()

pattern = re.compile("(\d+)d(\d+)([+-]\d+)?")

match_obj = re.match(pattern, args.roll)

if match_obj is None:
    raise ValueError(f"Invalid dice roll {args.roll}")

count, sides, bonus = [int(x) if x is not None else 0 for x in match_obj.groups()]

rolls = []
for c in range(count):
    r = random.randint(1, sides)
    rolls.append(r)

sum = sum(rolls) + bonus

if args.detailed:
    print(f"{args.roll} -> {rolls} + {bonus} = {sum}")
else:
    print(sum)
