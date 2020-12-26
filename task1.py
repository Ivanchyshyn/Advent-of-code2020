"""Find the two entries that sum to 2020"""
"""Find the three entries that sum to 2020"""


def get_result(values):
    for i, first in enumerate(values, 1):
        for second in values[i:]:
            if first + second == 2020:
                return first * second


def get_result_of_three(values):
    for i, first in enumerate(values, 1):
        for second in values[i:]:
            for third in values[i+1:]:
                if first + second + third == 2020:
                    return first * second * third


if __name__ == '__main__':
    with open('input_task1.txt') as f:
        values = f.read().strip().split('\n')

    values = list(map(int, values))
    print(get_result(values))
    print(get_result_of_three(values))
