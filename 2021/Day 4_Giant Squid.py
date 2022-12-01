import re
from pprint import pprint
f = open("day4.txt","r")
lines = f.readlines()

calls = lines[0]
calls = calls.strip('\n')
calls = calls.split(',')

print(calls)

boards = []
i = 1
for x in range(0, 100):
    boards.append([])
    for y in range(5):
        boards[x].append([])
        for z in range(5):
            if lines[i] == "\n":
                i = i + 1
            line = lines[i].strip('\n')
            line = re.split(r" {1,}", line)
            if '' in line:
                line.remove('')
            boards[x][y] = line
            i = i + 1
            if i > len(lines) - 1:
                break
        else:
            continue
        break
    else:
        continue
    break

pprint(boards)

# adding 100 to bingo tile to show that it has been.

def checkBingo(board):
    for row in board:
        res = True
        for val in row:
            if val // 100 != 1:
                res = False
        if res == True:
            return res
    for x in range(5):
        for y in range(5):
            if board[y][x] // 100 != 1:
                res = False
        if res == True:
            return res
    return False

def calculateScore(board):
    sum = 0
    for x in board:
        for y in row:
            if board[y][x] // 100 == 0:
                sum += board[y][x]
    return sum

results = []
for value in calls:
    for board in boards:
        for row in board:
            for val in range(len(row)):
                if value == val:
                    row[val-1] = str(int(val) + 100)
                    if checkBingo(board):
                        calculateScore(board)
                        results.append([value, sum])


pprint(results)