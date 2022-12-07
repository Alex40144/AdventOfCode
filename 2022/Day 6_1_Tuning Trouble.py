f = open("2022\inputs\day6.txt","r")
lines = f.readlines()
line = list(lines[0])

number = next(i for i in range(len(line)-1) if len(line[i: i + 4]) == len(set(line[i: i + 4])))

print(number + 4)
