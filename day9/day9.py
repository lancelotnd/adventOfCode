with open('input.txt') as f:
    lines = f.readlines()

def getConnexIndex(hsize,  index, array):
    toReturn = []
    if (index % hsize) != 0:
        toReturn.append(index-1)
    if (index - hsize) >= 0:
        toReturn.append(index-hsize)
    if (index + hsize) < len(array):
        toReturn.append(index+ hzise)
    if (index + 1) % hsize  != 0:
        toReturn.append(index+1)
    return toReturn

def getConnex(hsize,  index, array):
    toReturn = []
    if (index % hsize) != 0:
        toReturn.append(array[index-1])
    if (index - hsize) >= 0:
        toReturn.append(array[index-hsize])
    if (index + hsize) < len(array):
        toReturn.append(array[index+ hzise])
    if (index + 1) % hsize  != 0:
        toReturn.append(array[index+ 1])
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
    tmp  = [x for x in str(n)]
    for i in tmp:
        master.append(int(i))
mins = []
indexMin = []
for n in range(len(master)):
    connexe = getConnex(hzise, n, master)
    if master[n] < min(connexe):
        indexMin.append(n)
        mins.append(master[n])
totalSizes= []
for i in indexMin:
    visited = findBassine(i, hzise, master)
    totalSizes.append(len(visited))
totalSizes.sort(reverse=True)
final_list = totalSizes[0:3]
print("Answer is :",final_list[0] * final_list[1] * final_list[2])