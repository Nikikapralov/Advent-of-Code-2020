valid_passwords = []
while True:
    line = input()
    if line:
        two_points_in_data, letter_searched, password = line.split()
        letter = letter_searched[0]
        point_one, point_two = two_points_in_data.split('-')
        index_one = int(point_one) - 1
        index_two = int(point_two) - 1
        if (password[index_one] == letter and password[index_two] != letter) or (password[index_two] == letter and password[index_one] != letter):
            valid_passwords.append(password)
    else:
        break
print(len(valid_passwords))
