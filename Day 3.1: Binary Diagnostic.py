#include <stdio.h>
#include <stdlib.h>
#include <math.h>


f = open("day3.txt","r")
lines = f.readlines()

newLines = []

for column in range(0, len(lines[0]) - 3):
    common = 0
    for line in lines:
        if line[column] == '1':
            common += 1
        else:
            common -= 1
    if common > 0 :
        most = 1
    else:
        most = 0
    
    #remove numbers that don't start with that
    for i in range(0, len(lines) - 1):
        if int(lines[i][column]) == most:
            newLines.append(lines[i])
    lines = newLines
    newLines = []
    print(lines)
oxygenBin = lines[0]

f.close()
f = open("day3.txt","r")
lines = f.readlines()

for column in range(0, len(lines[0]) - 3):
    common = 0
    for line in lines:
        if line[column] == '1':
            common += 1
        else:
            common -= 1
    if common >= 0 :
        least = 0
    else:
        least = 1
    
    #remove numbers that don't start with that
    for i in range(0, len(lines) - 1):
        if int(lines[i][column]) == least:
            newLines.append(lines[i])
    lines = newLines
    newLines = []
    if len(lines) == 1:
        break
carbonBin = lines[0]

f.close()



oxygen = 0
carbon = 0
for i in range(0, len(oxygenBin) -3):
    if int(oxygenBin[i]) > 0:
        oxygen |= 2 ** (len(line)-(i)-2)
    if int(carbonBin[i]) > 0:
        carbon |= 2 ** (len(line)-(i)-2)
print(oxygen)
print(carbon)
print(oxygen * carbon);