Highest = 0

f = open("2022\inputs\day1.txt","r")
lines = f.readlines()

count = 0
for line in lines:
    if line == "\n":
        count = 0
    else:
        line = int(line)
        count = count + line
        if count > Highest:
            Highest = count
f.close()
print(Highest)
