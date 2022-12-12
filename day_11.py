import operator
import os

from pprint import pprint
from collections import defaultdict

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
    MAX_ROUNDS = 10000

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

    common_denominator = 1
    for divisor in divisible_mappings.values():
        common_denominator = common_denominator * divisor

    while rounds != MAX_ROUNDS:
        for k, v in mappings.items():
            inspect_mappings[k] += len(v)
            true_k, false_k = outcome_mappings[k]
            while v:
                item = v.pop(0)
                t = divisible_mappings[k]
                # PART 1
                # new_item = math.floor(operation_mappings[k][0](item, operation_mappings[k][1]) / 3)
                # PART 2
                new_item = operation_mappings[k][0](item, operation_mappings[k][1]) % common_denominator

                if new_item % divisible_mappings[k] == 0:
                    mappings[true_k].append(new_item)
                else:
                    mappings[false_k].append(new_item)

        rounds += 1

    second, first = sorted(inspect_mappings.values())[-2:]
    print(second, first, second * first)
    pprint(inspect_mappings)
