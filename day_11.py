import math
import operator
import os

from pprint import pprint
from collections import defaultdict
from typing import List

from consts import ROOT_DIR


if __name__ == '__main__':
    f_path = os.path.join(ROOT_DIR, "inputs", "day_11.txt")
    # f_path = os.path.join(ROOT_DIR, "inputs", "test.txt")

    ops = {
        "+": operator.add,
        "*": operator.mul,
        "old": operator.pow,
    }

    with open(f_path, "r") as f:
        text = f.read()

    monkeys = text.split("\n\n")
    mappings = defaultdict(list)
    operation_mappings = defaultdict(tuple)
    divisible_mappings = defaultdict(int)
    inspect_mappings = defaultdict(int)
    outcome_mappings = defaultdict(tuple)

    rounds = 0
    MAX_ROUNDS = 20

    # Initialise moneys with items
    for monkey in monkeys:
        lines = monkey.split("\n")

        line_1 = lines[0].replace(":", "").split(" ")
        line_2 = lines[1].replace(",", "").split(" ")
        line_3 = lines[2].split("old ")
        line_4, line_5, line_6 = lines[3].split(" "), lines[4].split(" "), lines[5].split(" ")

        monkey_num = int(line_1[-1])
        items = [int(c) for c in line_2 if c.isdigit()]
        operation = [c if c.isdigit() else c for c in line_3[1].split(" ")]
        test, true_monkey, false_monkey = int(line_4[-1]), int(line_5[-1]), int(line_6[-1])

        sign, value = operation

        mappings[monkey_num] = items
        if value == "old":
            operation_mappings[monkey_num] = (ops.get("old"), 2)
        else:
            operation_mappings[monkey_num] = (ops.get(sign), int(value))
        divisible_mappings[monkey_num] = test
        inspect_mappings[monkey_num] = 0
        outcome_mappings[monkey_num] = (true_monkey, false_monkey)

    while rounds != MAX_ROUNDS:
        for k, v in mappings.items():
            inspect_mappings[k] += len(v)
            true_k, false_k = outcome_mappings[k]
            while v:
                item = v.pop(0)
                # new_item = math.floor(operation_mappings[k][0](item, operation_mappings[k][1]) / 3)
                new_item = hash(math.floor(operation_mappings[k][0](item, operation_mappings[k][1])))

                if new_item % hash(divisible_mappings[k]) == 0:
                    mappings[true_k].append(new_item)
                else:
                    mappings[false_k].append(new_item)

        rounds += 1

    second, first = sorted(inspect_mappings.values())[-2:]
    print(second, first, second * first)
    print(divisible_mappings)
    # pprint(mappings)
    # pprint(inspect_mappings)

    # 0: 11 -> 3 else 2
    # 1: 7  -> 6 else 7
    # 2: 13 -> 3 else 5
    # 3: 5  -> 4 else 5
    # 4: 3  -> 1 else 7
    # 5: 17 -> 4 else 1
    # 6: 2  -> 2 else 0
    # 7: 19 -> 6 else 0

    # 0                             not divisible by 2, 19
    # 1 divisible by 3              not divisible by 17
    # 2 divisible by 2              not divisible by 11
    # 3 divisible by 11, 13
    # 4 divisible by 5, 17
    # 5 divisible by                not divisible by 5, 13
    # 6 divisible by 7, 19
    # 7 divisible by                not divisible by 3, 7
