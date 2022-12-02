
forward = 0
depth = 0
aim = 0
line = []


f = open("2021\inputs\day2.txt","r")
lines = f.readlines()

for line in lines:
    value = int(line[-2])
    if line[0] == 'f':
        forward += value
        depth += aim * value
    elif line[0] == 'u':
        aim -= value
    elif line[0] == 'd':
        aim += value

f.close()
print(forward)
print(depth)
print(forward*depth)
