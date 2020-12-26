current_group = ''
groups = []
while True:
    line = input()
    if line == 'Stop':
        groups.append(current_group)
        break
    elif line:
        current_group += line
    else:
        groups.append(current_group)
        current_group = ''

results = [set(items) for items in groups]
answer = [len(items) for items in results]
print(sum(answer))