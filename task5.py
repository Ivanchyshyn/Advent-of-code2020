"""What is the highest seat ID on a boarding pass?"""


def get_id(row, column):
    return row * 8 + column


def get_row(match):
    max_value = 127
    min_value = 0
    return get_value(match, 'F', min_value, max_value)


def get_column(match):
    max_value = 7
    min_value = 0
    return get_value(match, 'L', min_value, max_value)


def get_value(match, check_letter, min_value, max_value):
    for letter in match:
        if letter == check_letter:
            max_value = (max_value - min_value) // 2 + min_value
        else:
            min_value = (max_value - min_value) // 2 + 1 + min_value
    return min_value


def get_result(values):
    max_id = 0
    for board_pass in values:
        row_match = board_pass[:7]
        column_match = board_pass[7:]
        row = get_row(row_match)
        column = get_column(column_match)
        pass_id = get_id(row, column)
        max_id = max(max_id, pass_id)
    return max_id


def get_result_2(values):
    result = []
    for board_pass in values:
        row_match = board_pass[:7]
        column_match = board_pass[7:]
        row = get_row(row_match)
        column = get_column(column_match)
        pass_id = get_id(row, column)
        result.append(pass_id)
    result = set(result)
    min_value = min(result)
    max_value = max(result)
    for i in range(min_value, max_value):
        if i not in result:
            return i


if __name__ == '__main__':
    with open('input_task5.txt') as f:
        lines = f.read().strip().split('\n')

    print(get_result(lines))
    print(get_result_2(lines))
