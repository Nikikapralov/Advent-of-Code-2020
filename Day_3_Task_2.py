import math
grid = []
while True:
    line = list(input())
    if line:
        grid.append(line)
    else:
        break

results = []

def traversal(moves, down=1):
    moves_start_from_1_not_0_on_grid = moves + 1
    counter = down
    trees = 0
    first = True
    position = 0
    for index, item in enumerate(grid):
        if first:
            first = False
            continue
        if counter > 1:
            counter -= 1
            continue
        elif counter == 1:
            counter = down
            if position in range(len(item) - moves_start_from_1_not_0_on_grid, len(item) - 1):
                for item_1 in grid:
                    item_1_copy = item_1.copy()
                    item_1.extend(item_1_copy)
            position += moves
            if item[position] == '#':
                trees += 1
            else:
                continue
    results.append(trees)
    return trees


traversal(1, 1)
traversal(3, 1)
traversal(5, 1)
traversal(7, 1)
traversal(1, 2)

answer = math.prod(results)
print(answer)

