line = input()
valid_passwords = []
while line:
    range_of_chars, letter_searched, password = line.split()
    minimum, maximum = range_of_chars.split('-')
    minimum = int(minimum)
    maximum = int(maximum)
    letter = letter_searched[0]
    amount_letters = password.count(letter)
    if amount_letters in range(minimum, maximum + 1):
        valid_passwords.append(password)
    line = input()
print(len(valid_passwords))
