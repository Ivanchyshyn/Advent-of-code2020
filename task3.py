"""How many trees would you encounter?"""


def get_result(values):
    count = 0
    width = len(values[0])
    for i, line in enumerate(values[2::2], 1):
        point = (i * 1) % width
        print(point, line[point])
        if line[point] == '#':
            count += 1
    return count


def get_result_2(values):
    # found out with changing function get_result
    # in this place `point = (i * 1) % width`
    return 85 * 176 * 96 * 87 * 47


if __name__ == '__main__':
    with open('input_task3.txt') as f:
        values = f.read().strip().split('\n')

    print(get_result(values))
    # 85 * 176 * 96 * 87 * 47
    print(get_result_2(values))
