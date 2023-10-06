#!/usr/bin/env python3
import math
import random
import re
import sys

import roll

def get_params(count, sides):
    lowest = count
    highest = count * sides
    centre = (lowest + highest) / 2

    steps = []
    if count == 2:
        steps = [1] * (sides - 1)
    elif count == 3:
        n_a = (sides - 1)
        n_b = (sides - 2)

        for i in range(2, 2 + n_a):
            steps.append(i)

        for j in range(i - 2, i - 2 - n_b, -2):
            steps.append(j)

    else:
        raise NotImplementedError(f"No steps set for {count} dice rolled.")

    # capture current list before possible 0 insertion
    r = reversed(steps)

    # insert a 0 if centrepoint in not integer
    if centre != int(centre):
        steps.append(0)

    # step list is symetric but with sign flipped
    for i in r:
        steps.append(i * -1)

    print("DEBUG:", steps)

    return lowest, highest, centre, steps

def get_probabilities(lowest, highest, centre, steps):
    probabilities = {}
    x = 1
    for i, n in enumerate(range(lowest, highest)):
        probabilities[n] = x
        x += steps[i]

    # make sure to add last entry
    probabilities[highest] = x

    return probabilities

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--roll", default="1d6")
    parser.add_argument("-d", "--detailed", action="store_true")
    args = parser.parse_args()

    count, sides, mod = roll.parse_roll(args.roll)
    total_p = int(math.pow(sides, count))
    digits = math.ceil(math.log10(total_p))

    print(f"{args.roll} has {total_p} permutations with ...")

    lowest, highest, centre, steps = get_params(count, sides)
    probabilities = get_probabilities(lowest, highest, centre, steps)

    print(f"... {len(probabilities)} different values")

    for k, v in probabilities.items():
        k += mod
        print(f"{k:>3} x {v:>{digits}}")
