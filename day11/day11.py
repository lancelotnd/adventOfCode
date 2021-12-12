with open('test.txt') as f:
    lines = f.readlines()


def getConnexIndex(hsize,  index, array):
    toReturn = []
    if (index % hsize) != 0: #W   
        toReturn.append(index-1)
    if (index - hsize) >= 0: #N
        if(index-hsize+1) % hsize != 0: #NE
            toReturn.append(index - hsize + 1)
        if(index-hsize-1) % hsize >= 0 and (index-hsize-1) !=0: #NW
            toReturn.append(index-hsize - 1)
        toReturn.append(index-hsize)
    if (index + hsize) < len(array): #S
        toReturn.append(index + hzise)
        if ((index+hsize+1) < len(array)) and ((index+hsize+1) % hsize != 0): #SE
            toReturn.append(index+ hsize + 1)
        if(index+hsize-1) % hsize >= 0: #SW
            toReturn.append(index+hsize-1)
    if (index + 1) % hsize != 0:
        toReturn.append(index + 1)
    return toReturn

def stepOneIncrement(array:list):
    return [x+1 for x in array]

def flashAndIncrementAdjacent(array:list, hsize:int):
    unvisited = set()
    for i in range(len(array)):
        unvisited.add(i)
    while(len(unvisited) != 0):
        currentIndex = unvisited.pop()
        if array[currentIndex] > 9:
            to_increment = getConnexIndex(hsize, currentIndex, array)
            array[currentIndex] = 0 
            to_revisit = [x for x in to_increment if array[x] != 0]
            for octopus in to_revisit:
                array[octopus]+=1
                unvisited.add(octopus)
    return array


def printArray(array:list, hsize:int):
    row = []
    j = 0
    for i in range(len(array)):
        if j == hsize:
            print(*row)
            j = 0 
            row = []
        row.append(array[i])
        j+=1
    print(*row)
    return array



def getConnex(hsize,  index, array):
    toReturn = []
    if (index % hsize) != 0: #W   
        toReturn.append(array[index-1])
    if (index - hsize) >= 0: #N
        if(index-hsize+1) % hsize != 0: #NE
            toReturn.append(array[index- hsize + 1])
        if(index-hsize-1) % hsize !=0 and (index-hsize-1) !=0: #NW
            toReturn.append(array[index-hsize-1])
        toReturn.append(array[index-hsize])
    if (index + hsize) < len(array): #S
        toReturn.append(array[index + hzise])
        if index+hsize+1 < len(array) and (index+hsize+1) % hsize != 0: #SE
            toReturn.append(array[index+ hsize + 1])
        if(index+hsize-1) % hsize !=0: #SW
            toReturn.append(array[index+hsize-1])
    if (index + 1) % hsize != 0:
        toReturn.append(array[index + 1])
    return toReturn


def findBassine(initialIndex, hsize, array):
    visited = set()
    unvisited = {initialIndex}
    while(len(unvisited) != 0):
        connexe = []
        to_visit = unvisited.pop()
        visited.add(to_visit)
        connexe = getConnexIndex(hsize, to_visit, array)
        connexe = [x for x in connexe if x not in visited]
        connexe = [x for x in connexe if array[x] != 9]
        for e in connexe:
            unvisited.add(e)
    return list(visited)


m = [l.replace('\n', '') for l in lines]
hzise = len(str(m[0]))
vsize = len(m)

master = []
for n in m:
    tmp = [x for x in str(n)]
    for i in tmp:
        master.append(int(i))


for i in range(len(master)):
    print(i, getConnexIndex(hzise, i, master))
"""

totalFlashes = 0
for i in range(11):
    print("After step", f"{str(i)}:", totalFlashes)
    printArray(master, hzise)
    master = stepOneIncrement(master)
    master = flashAndIncrementAdjacent(master, hzise)
    totalFlashes += len([x for x in master if x == 0])

print("Answer, total number of flashes : ", totalFlashes)
    
"""


