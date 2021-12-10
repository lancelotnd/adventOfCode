with open('input.txt') as f:
    lines = f.readlines()


def getConnex(hsize,  index, array):
    toReturn = []
    if index % hsize != 0:
        toReturn.append(array[index-1])
    if index - hsize >= 0:
        toReturn.append(array[index-hsize])
    if index + hsize < len(array):
        toReturn.append(array[index+ hzise])
    if index + 1 % hsize  != 0:
        toReturn.append(array[index+ 1])
    return toReturn


m = [int(l.replace('\n', '')) for l in lines]    
hzise = len(str(m[0]))
vsize = len(m)
master = []
for n in m:
    tmp  = [x for x in str(n)]
    for i in tmp:
        master.append(int(i))

mins = []

for n in range(0, len(master)-1):
    if master[n] < min(getConnex(hzise, n, master)):
        mins.append(master[n])


print("answer",sum([x+1 for x in mins]))