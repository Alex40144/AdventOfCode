previous = 9999
count = 0

f = open("day1.txt","r")
lines = f.readlines()

for line in lines:
    line = int(line)
    if (line > previous):
        count += 1
    previous = line

f.close()
print(count)
