"""How many passports are valid?"""
import re

required_fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
HGT_PATTERN = re.compile('(\d+)((cm)|(in))$')
HCL_PATTERN = re.compile('#[0-9a-f]{6}$')
PID_PATTERN = re.compile('\d{9}$')
ECL = set('amb blu brn gry grn hzl oth'.split())


def get_result(passwords):
    count = 0
    for password in passwords:
        if not (required_fields - set(password)):
            count += 1
    return count


def get_result_2(passwords):
    count = 0
    for password in passwords:
        if not (required_fields - set(password)):
            for key, value in password.items():
                if not validate[key](value):
                    break
            else:
                count += 1
    return count


def validate_byr(value):
    try:
        value = int(value)
        return 1920 <= value <= 2002
    except (TypeError, ValueError):
        return False


def validate_iyr(value):
    try:
        value = int(value)
        return 2010 <= value <= 2020
    except (TypeError, ValueError):
        return False


def validate_eyr(value):
    try:
        value = int(value)
        return 2020 <= value <= 2030
    except (TypeError, ValueError):
        return False


def validate_hgt(value):
    match = HGT_PATTERN.match(value)
    if match:
        val = int(match.group(1))
        metric = match.group(2)
        if metric == 'cm':
            return 150 <= val <= 193
        else:
            return 59 <= val <= 76


def validate_hcl(value):
    return bool(HCL_PATTERN.match(value))


def validate_ecl(value):
    return value in ECL


def validate_pid(value):
    return bool(PID_PATTERN.match(value))


if __name__ == '__main__':
    with open('input_task4.txt') as f:
        lines = f.readlines()
        passwords = []
        password = {}
        for line in lines:
            line = line.strip()
            if not line:
                passwords.append(password)
                password = {}
            values = line.split()
            for info in values:
                key, value = info.split(':', 1)
                password[key] = value

    validate = {
        'byr': validate_byr,
        'iyr': validate_iyr,
        'eyr': validate_eyr,
        'hgt': validate_hgt,
        'hcl': validate_hcl,
        'ecl': validate_ecl,
        'pid': validate_pid,
        'cid': lambda x: True,
    }
    print(get_result(passwords))
    print(get_result_2(passwords))
