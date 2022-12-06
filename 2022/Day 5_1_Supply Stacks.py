f = open("2022\inputs\day5.txt","r")
lines = f.readlines()

state = 0
stack = []
for line in lines:
    line = line.strip("\n")
    if (line.startswith(" 1")):
        state = 1

        continue
    if(line == ""):
        # rotate list
        stack = list(zip(*stack[::-1]))
        stack = [list(i) for i in stack]
        print(stack)
        continue
    #load crates into array
    if (state == 0):
     
        stack.append([line[i] for i in range(1, len(line), 4)])
        print(stack)
    if (state == 1):
        line = line.split(' ')
        mo = int(line[1])
        fr = int(line[3]) - 1
        to = int(line[5]) - 1
        print(line)
        for i in range(0, mo):
            fromIndex   = ''.join(stack[fr]).rindex(next(s for s in reversed(stack[fr]) if (s != ' ')))
            try:
                toIndex = stack[to].index(next(s for s in stack[to] if (s == ' ')))
            except:
                stack[to].append(' ')
                toIndex = len(stack[to]) - 1

            print(str(fromIndex) + " " + str(toIndex))
            stack[to][toIndex] = stack[fr][fromIndex]
            stack[fr][fromIndex] = ' '

            print(stack)

    
top = ''
for col in stack:
    top += col[col.index(next(s for s in reversed(col) if s != ' '))]

print(top)

#list of guesses
#DBGHDJDGG