#!/usr/bin/env python3
import argparse
import math
import random
import re
import sys

parser = argparse.ArgumentParser()
parser.add_argument("-r", "--roll", default="1d6")
parser.add_argument("-d", "--detailed", action="store_true")
args = parser.parse_args()

pattern = re.compile("(\d+)d(\d+)([+-]\d+)?")

def permute(head, tail):
    if len(tail) == 0:
        return head

    permutations = []

    for n in head:
        for p in permute(tail[0], tail[1:]):
            if type(p) == int:
                p = [p]

            permutations.append([n] + p)

    return permutations

match_obj = re.match(pattern, args.roll)

if match_obj is None:
    raise ValueError(f"Invalid dice roll {args.roll}")

count, sides, bonus = [int(x) if x is not None else 0 for x in match_obj.groups()]
total_p = int(math.pow(sides, count))
digits = math.ceil(math.log10(total_p))

if count == 1:
    # print(f"Refusing to calculate permutations of a single dice roll.")
    print(f"Range of values for {args.roll} is {1 + bonus} to {sides + bonus} with equal probability.")
    sys.exit()

print(f"{args.roll} has {total_p} permutations with ...")

head = range(1, sides + 1)
tail = [head] * (count - 1)

permutations = permute(head, tail)
sums = {}
for p in permutations:
    s = sum(p)
    if s not in sums:
        sums[s] = 0
    sums[s] += 1


print(f"... {len(sums)} different values")

for k, v in sums.items():
    k += bonus
    print(f"{k:>3} x {v:>{digits}}")
