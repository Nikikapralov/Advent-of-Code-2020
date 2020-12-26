numbers = []

while True:
    line = input()
    if not line:
        break
    else:
        numbers.append(int(line))

for index, number in enumerate(numbers):
    for second_number in range(index + 1, len(numbers)):
        if number + numbers[second_number] == 2020:
            result = number * numbers[second_number]
            print(f'{result}, number_1 = {number}, number_2 = {second_number}')
