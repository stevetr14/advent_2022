import math
import os


def part_1(data):
    digits = {
        "2": 2,
        "1": 1,
        "0": 0,
        "-": -1,
        "=": -2,
    }
    reversed_digits = {
        2: "2",
        1: "1",
        0: "0",
        -1: "-",
        -2: "=",
    }
    total = 0

    for x in data:
        value = x.strip()
        decimal = 0
        for idx, c in enumerate(value, start=1):
            power = len(value) - idx
            decimal += digits.get(c) * 5**power
        total += decimal

    snafu = ""
    # Log decimal value to base 5 to determine the number of digits needed
    starting_power = round(math.log(total, 5))

    # Reverse decimal back to SNAFU base
    for i in range(starting_power, -1, -1):
        multiplier = round(total / 5**i)  # The snafu digit is rounded
        snafu_digit = reversed_digits.get(multiplier)
        snafu += snafu_digit
        total -= multiplier * 5**i
    print(snafu)


if __name__ == '__main__':
    f_path = os.path.join("inputs", "day_25.txt")
    # f_path = os.path.join("inputs", "test.txt")

    with open(f_path, "r") as f:
        text = f.readlines()

    part_1(text)
