f = open("2022\inputs\day2.txt","r")
lines = f.readlines()

score = 0

winmap = { "A": "Y", "B": "Z", "C": "X"}
drawmap = { "A": "X", "B": "Y", "C": "Z"}
losemap = { "A": "Z", "B": "X", "C": "Y"}
for line in lines:
    # split line into two actions
    data = line.split(" ")

    #strip data to first char (remove new line)
    opponent = data[0][0] 
    outcome = data[1][0]

    #win
    if outcome == "X": 
        play = losemap[opponent]
    elif outcome == "Y":
        play = drawmap[opponent]
    else:
        play = winmap[opponent]
    
    #add score for selected action
    if play == "X":
        score += 1
    elif play == "Y":
        score += 2
    elif play == "Z":
        score += 3

    #add score for win case

    if (opponent == "A" and play == "Y") or (opponent == "B" and play == "Z") or (opponent == "C" and play == "X"):
        score += 6

    #add score for draw

    if (opponent == "A" and play == "X") or (opponent == "B" and play == "Y") or (opponent == "C" and play == "Z"):
        score += 3
print(score)