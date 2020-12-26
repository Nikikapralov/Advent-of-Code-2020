current_group = []
groups = []
result = 0
while True:
    line = input()
    if line == 'Stop':
        groups.append(current_group)
        break
    elif line:
        current_group.append(line)
        pass
    else:
        groups.append(current_group)
        current_group = []
        pass
print(groups)

for group in groups:
    is_done = False
    for person in group:
        if is_done:
            continue
        elif len(group) > 1:
            for answer in person:
                is_first = True
                counter = 0
                for check in group:
                    if is_first:
                        is_first = False
                        continue
                    else:
                        if answer in check:
                            counter += 1
                            continue
                if counter == len(group) - 1:
                    result += 1
                is_done = True
        else:
            result += len(person)

print(result)

