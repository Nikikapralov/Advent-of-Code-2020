import math
line = input()
list_of_ids = []


def determine_id(coloumn, row):
    id = row * 8 + coloumn
    return id


def row(data):
    upper_point = 127
    lower_point = 0
    current_point = 127
    for direction in data:
        current_point = upper_point - lower_point
        if direction == 'F':  # lower half
            current_point = math.floor(current_point / 2)
            if current_point >= lower_point:
                upper_point = current_point
            else:
                upper_point = lower_point + current_point
        elif direction == 'B':  # upper half
            current_point = math.floor(current_point / 2)
            if current_point <= upper_point:
                lower_point = upper_point - current_point
            else:
                lower_point = current_point
    return upper_point



def coloumn(data):
    upper_point = 7
    lower_point = 0
    current_point = 7
    for direction in data:
        current_point = upper_point - lower_point
        if direction == 'L':
            current_point = math.floor(current_point / 2)
            if current_point >= lower_point:
                upper_point = current_point
            else:
                upper_point = lower_point + current_point
        elif direction == 'R':
            current_point = math.floor(current_point / 2)
            if current_point <= upper_point:
                lower_point = upper_point - current_point
            else:
                lower_point = current_point
    return lower_point



while line:
    row_line = line[:7]
    coloumn_line = line[7:]
    x = row(row_line)
    print(x)
    y = coloumn(coloumn_line)
    print(y)
    result = determine_id(y, x)
    list_of_ids.append(result)
    line = input()

print(max(list_of_ids))
