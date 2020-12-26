import re
pattern = r'\b\w+|\W+'
passport = ''
all_passports = []
valid_passports = []


def is_passport_valid(passport):
    if 'byr' in passport and 'iyr' in passport and 'eyr' in passport and 'hgt' in passport and 'hcl' in passport and 'ecl' in passport and 'pid' in passport:
        return True
    else:
        return False


while True:
    data = input()
    if data and data != 'Stop':
        passport += data + ' '
    elif data == 'Stop':
        all_passports.append(passport)
        break
    else:
        all_passports.append(passport)
        passport = ''

for item in all_passports:
    result = re.findall(pattern, item)
    if is_passport_valid(result):
        valid_passports.append(result)

print(len(valid_passports))
