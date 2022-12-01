Highest = []

f = open("./2022/day1.txt","r")
lines = f.readlines()

count = 0
for line in lines:
    if line == "\n":
        Highest.append(count)
        count = 0
    else:
        line = int(line)
        count = count + line
f.close()

Highest.sort(reverse=True)
print(Highest)

print(Highest[0] + Highest[1] + Highest[2])