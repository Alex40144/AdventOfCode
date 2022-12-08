f = open("2022\inputs\example\day8.txt","r")
lines = f.readlines()
Hscore = 0
grid = []
for line in lines:
    line = line.strip("\n")
    line = [*line]
    line = [int(s) for s in line]
    grid.append(line)
print(grid)

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
        print("new tree")
        print(treeValue)
        score = 1
        for dist in range(len(up)):
            if (up[dist] >= treeValue):
                print(dist + 1)
                score *= dist + 1
                break
        for dist in range(len(down)):
            if (down[dist] >= treeValue):
                print(dist + 1)
                score *= dist + 1
                break
        for dist in range(len(left)):
            if (left[dist] >= treeValue):
                print(dist + 1)
                score *= dist + 1
                break
        for dist in range(len(right)):
            if (right[dist] >= treeValue):
                print(dist + 1)
                score *= dist + 1
                break
        print(score)
        if score > Hscore:
            Hscore = score
print(Hscore)