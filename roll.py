#!/usr/bin/env python3
import random
import re

def parse_roll(roll):
    pattern = "(\d+)d(\d+)([+-]\d+)?"
    match_obj = re.match(pattern, roll)

    if match_obj is None:
        raise ValueError(f"Invalid dice roll {roll}")

    count, sides, mod = [int(x) if x is not None else 0 for x in match_obj.groups()]
    return count, sides, mod

def roll_dice(count, sides, mod):
    rolls = []
    for c in range(count):
        r = random.randint(1, sides)
        rolls.append(r)

    total = sum(rolls) + mod

    return rolls, total

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--roll", default="1d6")
    parser.add_argument("-d", "--detailed", action="store_true")
    args = parser.parse_args()

    count, sides, mod = parse_roll(args.roll)
    rolls, total = roll_dice(count, sides, mod)

    if args.detailed:
        a = min(rolls)
        b = max(rolls)
        print(f"{args.roll} -> {rolls} + {mod} = {total} (lowest: {a}, highest: {b})")
    else:
        print(total)
