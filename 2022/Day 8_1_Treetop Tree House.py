f = open("2022\inputs\day8.txt","r")
lines = f.readlines()

grid = []
for line in lines:
    line = line.strip("\n")
    line = [*line]
    line = [int(s) for s in line]
    grid.append(line)
print(grid)

#loop through every tree
#work out it tree is visable.
#split into 4 lists. see it highest value
visible = 0
for row in range(len(grid)):
    for tree in range(len(grid[row])):
        column = []
        for s in range(len(grid)):
            column.append(grid[s][tree])
        up = column[:row]
        down = column[(row + 1)::]
        left = grid[row][:tree]
        right = grid[row][(tree+1)::]
        treeValue = grid[row][tree]
        if (treeValue > max(up, default=-1) or treeValue > max(down, default=-1) or treeValue > max(left, default=-1) or treeValue > max(right, default=-1)):
            print(treeValue)
            visible += 1

print(visible)