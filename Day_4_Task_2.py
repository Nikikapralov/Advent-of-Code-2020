import re
pattern = r'(?P<byr>byr:(192[0-9]|19[3-9][0-9]|200[0-2]))($|(?=\s))|(?P<iyr>iyr:(201[0-9]|2020))($|(?=\s))|(?P<eyr>eyr:(202[0-9]|2030))($|(?=\s))|(?P<hgt>hgt:((((15[0-9]|1[6-8][0-9]|19[0-3])cm)|((59|6[0-9]|7[0-6])in))))($|(?=\s))|(?P<hcl>hcl:#[0-9a-f]{6})($|(?=\s))|(?P<ecl>ecl:((amb)|(blu)|(brn)|(gry)|(grn)|(hzl)|(oth)))($|(?=\s))|(?P<pid>pid:[0-9]{9})($|(?=\s))'
passport = ''
all_passports = []
valid_passports = []

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
    result = re.finditer(pattern, item)
    current_passport = []
    for x in result:
        dictionary = x.groupdict()
        if dictionary['pid'] is not None:
            current_passport.append(dictionary['pid'])
        elif dictionary['hgt'] is not None:
            current_passport.append(dictionary['hgt'])
        elif dictionary['ecl'] is not None:
            current_passport.append(dictionary['ecl'])
        elif dictionary['iyr'] is not None:
            current_passport.append(dictionary['iyr'])
        elif dictionary['eyr'] is not None:
            current_passport.append(dictionary['eyr'])
        elif dictionary['byr'] is not None:
            current_passport.append(dictionary['byr'])
        elif dictionary['hcl'] is not None:
            current_passport.append(dictionary['hcl'])
    if len(current_passport) == 7:
        valid_passports.append(current_passport)

print(len(valid_passports))
