import re

pattern_starting_bag = r'^[a-z]+\s[a-z]+ bag'
pattern_bags_inside = r'(?P<amount>[0-9]+)\s(?P<bag>\w+\s\w+ bag)|(?P<no_bag>no\s\w+ bag)'
total_data = []

while True:
    data = input()
    if not data:
        break
    else:
        total_data.append(data)

starting_bags = []
bags_inside_temp = []
bags_inside = []

for piece in total_data:
    result_start = re.findall(pattern_starting_bag, piece)
    result_inside = re.finditer(pattern_bags_inside, piece)
    bags_in_row = []
    for item in result_inside:
        dictionary = item.groupdict()
        bags_in_row.append(dictionary)
    starting_bags.append(result_start)
    bags_inside_temp.append(bags_in_row)

for bags_per_row in bags_inside_temp:
    bags_per_row_list = []
    for item in bags_per_row:
        if not item['no_bag']:
            new_dict = {item['bag']: item['amount']}
            bags_per_row_list.append(new_dict)
        else:
            bags_per_row_list.append('no other bag')
    bags_inside.append(bags_per_row_list)

zip_starting_bags_bags_inside = zip(starting_bags, bags_inside)

final_data_arrangement = {}

for x in zip_starting_bags_bags_inside:
    final_data_arrangement["".join(x[0])] = x[1]

for key, value in final_data_arrangement.items():
    if key == 'shiny gold bag':
        starting_point = value

total_amount_of_bags = []


def tree(starting_point, total_amount_branch=1):
    for point in starting_point:
        if point == 'no other bag':
            total_amount_of_bags.append(total_amount_branch)
            return
        else:
            for key, amount in point.items():
                new_starting_point = final_data_arrangement[key]
                tree(new_starting_point, total_amount_branch * int(amount))
    total_amount_of_bags.append(total_amount_branch)


tree(starting_point, total_amount_branch=1)
print(sum(total_amount_of_bags) - 1)
print(total_amount_of_bags)