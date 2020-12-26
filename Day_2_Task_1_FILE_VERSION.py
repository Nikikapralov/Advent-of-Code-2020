valid_passwords = []
with open('Advent.txt', 'r') as file:
    data = file.read()
    split_data = data.split('\n')
    for line in split_data:
        range_of_chars, letter_searched, password = line.split()
        minimum, maximum = range_of_chars.split('-')
        minimum = int(minimum)
        maximum = int(maximum)
        letter = letter_searched[0]
        amount_letters = password.count(letter)
        if amount_letters in range(minimum, maximum + 1):
            valid_passwords.append(password)
    print(len(valid_passwords))
