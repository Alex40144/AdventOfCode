#include <stdio.h>
#include <stdlib.h>

previous = [0,0,0]
previousSum = 999
sum;
count = 0;

f = open("2021\inputs\day1.txt","r")
lines = f.readlines()

for line in lines:
    line = int(line)
    previous[2] = previous [1]
    previous[1] = previous[0]
    previous[0] = line

    if (previous[2] == 0):
        continue

    sum = previous[2] + previous[1] + previous[0]

    if (sum > previousSum):
        count += 1;
    previousSum = sum


f.close()
print(count)
