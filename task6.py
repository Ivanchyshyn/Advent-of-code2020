"""What is the sum of common counts?"""


def get_result(lines):
    total = 0
    letters = set()
    for line in lines:
        line = line.strip()
        if line:
            letters.update(line)
        else:
            total += len(letters)
            letters = set()
    total += len(letters)
    return total


def get_result_2(lines):
    total = 0
    common_letters = set()
    first = True
    for line in lines:
        line = line.strip()
        if line:
            if first:
                common_letters.update(line)
                first = False
            else:
                common_letters.intersection_update(line)
        else:
            total += len(common_letters)
            common_letters = set()
            first = True
    total += len(common_letters)
    return total


if __name__ == '__main__':
    with open('input_task6.txt') as f:
        lines = f.readlines()

    print(get_result(lines))
    print(get_result_2(lines))
