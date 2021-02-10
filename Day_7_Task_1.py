import re
pattern = r'\w+ \w+ bag'
total_data = []

while True:
    data = input()
    if not data:
        break
    else:
        total_data.append(data)
bags = []

for piece in total_data:
    result = re.findall(pattern, piece)
    bags.append(result)
list_of_dicts = []

for bag in bags:
    dictionary = {bag[0]: [bag[item] for item in range(1, len(bag))]}
    list_of_dicts.append(dictionary)


starting_points = []

for dict_bag in list_of_dicts:
    for key, value in dict_bag.items():
        if "shiny gold bag" in value:
            starting_points.append(key)

colours_holding_a_gold_bag = set()


def tree(starting_points):
    for point in starting_points:
        if point == "no other bag":
            return
        elif point == 'shiny gold bag':
            continue
        elif point in colours_holding_a_gold_bag:
            continue
        else:
            colours_holding_a_gold_bag.add(point)
            for dict_bag in list_of_dicts:
                for key, value in dict_bag.items():
                    if point in value:
                        new_starting_point = [key]
                        tree(new_starting_point)

tree(starting_points)

print(len(colours_holding_a_gold_bag))