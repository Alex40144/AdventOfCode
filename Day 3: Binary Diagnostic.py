#include <stdio.h>
#include <stdlib.h>
#include <math.h>
common = [0,0,0,0,0,0,0,0,0,0,0,0]

line = []


f = open("day3.txt","r")
lines = f.readlines()

for line in lines:
    for i in range(0, len(line) -1):
        if line[i] == '1':
            common[i] += 1
        else:
            common[i] -= 1
f.close()
gamma = 0
epsilon = 0
for i in range(0, len(line) -1):
    if common[i] > 0 :
        print(2**i)
        gamma |= 2 ** (len(line)-(i)-2)
    else:
        epsilon |= 2 ** (len(line)-(i)-2)
print(gamma)
print(epsilon)
print(gamma * epsilon);