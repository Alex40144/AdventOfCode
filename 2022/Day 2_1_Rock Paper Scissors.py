f = open("2022\inputs\day2.txt","r")
lines = f.readlines()

score = 0
for line in lines:
    # split line into two actions
    data = line.split(" ")

    #strip data to first char (remove new line)
    opponent = data[0][0]
    player = data[1][0]

    #add score for selected action
    if player == "X":
        score += 1
    elif player == "Y":
        score += 2
    elif player == "Z":
        score += 3

    #add score for win case

    if (opponent == "A" and player == "Y") or (opponent == "B" and player == "Z") or (opponent == "C" and player == "X"):
        score += 6

    #add score for draw

    if (opponent == "A" and player == "X") or (opponent == "B" and player == "Y") or (opponent == "C" and player == "Z"):
        score += 3
print(score)