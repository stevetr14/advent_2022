import os
from ast import literal_eval

from consts import ROOT_DIR


def flatten(array: list, count: int):
    if not array:
        return array, count

    if isinstance(array[0], list):
        a, a_len = flatten(array[0], count)
        b, b_len = flatten(array[1:], count)
        # return flatten(array[0]) + flatten(array[1:])
        return a + b, a_len + b_len

    c, c_len = flatten(array[1:], count)
    # return array[:1] + flatten(array[1:])
    return array[:1] + c, count


if __name__ == '__main__':
    # f_path = os.path.join(ROOT_DIR, "inputs", "day_13.txt")
    f_path = os.path.join(ROOT_DIR, "inputs", "test.txt")

    with open(f_path, "r") as f:
        text = f.read().split("\n\n")

    # all_pairs = [literal_eval(line) for line in text if line.strip() != ""]
    #
    # for pair in all_pairs:
    #     print(pair)

    index_sum = 0

    for index, line in enumerate(text):
        first, second = line.split("\n")
        p_1, p_2 = literal_eval(first), literal_eval(second)

        new_p_1, size_1 = flatten(p_1, 1)
        new_p_2, size_2 = flatten(p_2, 1)
        # print(index + 1, new_p_1, new_p_2)
        # print(index + 1, p_1, size_1, p_2, size_2)

        is_right_order = False
        done = False

        while len(new_p_1) != 0 and len(new_p_2) != 0:
            left = new_p_1.pop(0)
            right = new_p_2.pop(0)

            if right > left:
                print(index + 1)
                index_sum += (index + 1)
                is_right_order = True
            elif left > right:
                done = True

        if not is_right_order and len(new_p_1) == len(new_p_2):
            if size_2 > size_1:
                print(index + 1)
                index_sum += (index + 1)
                is_right_order = True

        if done:
            break

        if len(new_p_2) > len(new_p_1):
            print(index + 1)
            index_sum += (index + 1)
            is_right_order = True

    # print(index_sum)
