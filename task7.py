"""How many color bags contain `shiny gold bag`?"""
import re

BAG_REGEX = re.compile(r'(\w+\s*\w+)\s+bags')


def get_result(lines):
    total = 0
    return total


def get_result_2(lines):
    total = 0
    return total


if __name__ == '__main__':
    with open('input_task7.txt') as f:
        bags = []
        for line in f:
            if not line.strip():
                continue
            bag, can_contain = line.split(' contain ', 1)
            contain_bags = []
            for contain_bag in can_contain.split(','):
                _bag = BAG_REGEX.search(contain_bag)
                if _bag:
                    contain_bags.append(_bag.group(1))
            bags.append({BAG_REGEX.search(bag).group(1): contain_bags})

    print(bags)
    # print(get_result(lines))
    # print(get_result_2(lines))
