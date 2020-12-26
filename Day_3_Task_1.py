grid = []
while True:
    line = list(input())
    if line:
        grid.append(line)
    else:
        break
trees = 0
first = True
position = 0
for item in grid:
    item_copy = item.copy()
    if first:
        first = False
        continue
    if position in range(len(item) - 4, len(item) - 1):
        for item_1 in grid:
            item_1_copy = item_1.copy()
            item_1.extend(item_1_copy)
    position += 3
    if item[position] == '#':
        trees += 1
    else:
        continue
print(trees)

