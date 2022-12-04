f = open("2022\inputs\day4.txt","r")
lines = f.readlines()

score = 0
for line in lines:
    elfs = line.split(",")
    elfs[1] = elfs[1].strip("\n").split("-")
    elfs[0] = elfs[0].split("-")
    elfs = [list( map(int,i) ) for i in elfs] #convert to int
    if((elfs[0][0] >= elfs[1][0] and elfs[0][1] <= elfs[1][1]) or (elfs[1][0] >= elfs[0][0] and elfs[1][1] <= elfs[0][1] )):
        print(elfs)
        score += 1

print(score)