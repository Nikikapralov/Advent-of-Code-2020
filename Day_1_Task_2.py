numbers = []

while True:
    line = input()
    if not line:
        break
    else:
        numbers.append(int(line))

for index, number in enumerate(numbers):
    for second_number_index in range(index + 1, len(numbers)):
        for third_number_index in range(second_number_index + 1, len(numbers)):
            if number + numbers[second_number_index] + numbers[third_number_index] == 2020:
                result = number * numbers[second_number_index] * numbers[third_number_index]
                print(result)