import os
from pprint import pprint

import numpy as np

from consts import ROOT_DIR


if __name__ == '__main__':
    f_path = os.path.join(ROOT_DIR, "inputs", "day_8.txt")
    # f_path = os.path.join(ROOT_DIR, "inputs", "test.txt")

    with open(f_path, "r") as f:
        rows = [[int(c) for c in list(line.strip())] for line in f.readlines()]
        cols = [list(i) for i in zip(*rows)]

        row_num = len(rows)
        col_num = len(cols)

        test = np.copy(rows)
        test_2 = np.copy(cols)

        # PART 1
        # for i in range(1, row_num - 1):
        #     visible = False
        #     for j in range(1, col_num - 1):
        #         current_tree = rows[i][j]
        #         left = rows[i][:j]
        #         right = rows[i][j + 1:]
        #         reversed(left)
        #
        #         visible = all([x < current_tree for x in reversed(left)])
        #         if visible:
        #             test[i][j] = 1
        #             continue
        #
        #         visible = all([x < current_tree for x in right])
        #         if visible:
        #             test[i][j] = 1
        #             continue
        #         test[i][j] = -1

        # for i in range(1, col_num - 1):
        #     for j in range(1, row_num - 1):
        #         current_tree = cols[i][j]
        #         top = cols[i][:j]
        #         bottom = cols[i][j + 1:]
        #         reversed(top)
        #
        #         visible = all([x < current_tree for x in reversed(top)])
        #         if visible:
        #             test_2[i][j] = 1
        #             continue
        #
        #         visible = all([x < current_tree for x in bottom])
        #         if visible:
        #             test_2[i][j] = 1
        #             continue
        #
        #         test_2[i][j] = -1

        # t_test_2 = list(zip(*test_2))
        # final = np.add(test, t_test_2)
        #
        # print((final >= 0).sum())

        # PART 2
        for i in range(1, row_num - 1):
            visible = False
            for j in range(1, col_num - 1):
                current_tree = rows[i][j]
                left = rows[i][:j]
                right = rows[i][j + 1:]

                left_score = 0
                right_score = 0

                for x in reversed(left):
                    if x < current_tree:
                        left_score += 1
                    elif x >= current_tree:
                        left_score += 1
                        break

                for x in right:
                    if x < current_tree:
                        right_score += 1
                    elif x >= current_tree:
                        right_score += 1
                        break

                test[i][j] = left_score * right_score

        for i in range(1, col_num - 1):
            for j in range(1, row_num - 1):
                current_tree = cols[i][j]
                top = cols[i][:j]
                bottom = cols[i][j + 1:]

                top_score = 0
                bottom_score = 0

                for x in reversed(top):
                    if x < current_tree:
                        top_score += 1
                    elif x >= current_tree:
                        top_score += 1
                        break

                for x in bottom:
                    if x < current_tree:
                        bottom_score += 1
                    elif x >= current_tree:
                        bottom_score += 1
                        break

                test_2[i][j] = top_score * bottom_score

        t_test_2 = list(zip(*test_2))
        final = np.multiply(test, t_test_2)
        pprint(np.max(final[1:-1, 1:-1]))
