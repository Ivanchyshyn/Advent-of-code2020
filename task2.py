"""How many passwords are valid according to their policies?"""


def get_result(values):
    count = 0
    for string in values:
        policy, password = string.split(':', 1)
        policy, password = policy.strip(), password.strip()

        times, letter = policy.split(' ', 1)
        min_time, max_time = times.split('-')
        min_time, max_time = int(min_time), int(max_time)
        occurrence = password.count(letter)
        if min_time <= occurrence <= max_time:
            count += 1
    return count


def get_result_2(values):
    count = 0
    for string in values:
        policy, password = string.split(':', 1)
        policy, password = policy.strip(), password.strip()

        times, letter = policy.split(' ', 1)
        first_index, second_index = times.split('-')
        first_index, second_index = int(first_index) - 1, int(second_index) - 1
        if (
            (password[first_index] == letter and password[second_index] != letter) or
            (password[second_index] == letter and password[first_index] != letter)
        ):
            count += 1
    return count


if __name__ == '__main__':
    with open('input_task2.txt') as f:
        values = f.read().strip().split('\n')

    print(get_result(values))
    print(get_result_2(values))
