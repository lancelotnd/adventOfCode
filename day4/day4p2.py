with open('input.txt') as f:
    lines = f.readlines()

def isWinning(board, allNumbers):
    results = False
    i = 0
    while (i < 25):
         results = results or all(elem in allNumbers for elem in board[i:i+5])
         
         i += 5
    return results


def split(list_a, chunk_size):

    for i in range(0, len(list_a), chunk_size):
        yield list_a[i:i + chunk_size]


allNumbers = lines[0].split(',')
allNumbers = [x.replace('\n', '') for x in allNumbers]
allNumbers = [int(x) for x in allNumbers]

lines.pop(0)
nonEmpty = []
for l in lines:
    if len(l) > 1:
        nonEmpty.append(l)
master = []

i = 0
j = 0


for l in nonEmpty:
    l = l.replace('\n', '')
    m =  l.split(' ')
    g = [int(x) for x in m if x != '' ]
    master.append(g)


i = 0

boards = [[] for i in range(int(len(master)/5))]

for l in master:
    boards[int((i - (i % 5) )/5)].append(l)
    i+=1



for b in boards:
    for i in range(5):
        l = []
        for r in b[0:5]:
            l.append(r[i])
        b.append(l)


draw = []
draw.append(allNumbers.pop(0))
draw.append(allNumbers.pop(0))
draw.append(allNumbers.pop(0))
draw.append(allNumbers.pop(0))
draw.append(allNumbers.pop(0))
allBoardsStatus = [False] * len(boards)
print(allBoardsStatus)
foundBingo = False
while  foundBingo == False:
    draw.append(allNumbers.pop(0))
    i = 0
    for b in boards:
        for r in b:
            foundBingo =  all(elem in draw  for elem in r)
            if(foundBingo):
                allBoardsStatus[i] = True
                if(all(allBoardsStatus)):
                    totalSum = 0
                    for remain in b[0:5]:
                        print(remain)
                        for n in remain:
                            if n not in draw:
                                totalSum += n
                    print("Last board to win at ",r, "with", draw)
                    print("Board no",i)
                    print(totalSum)
                    print(draw[-1])
                    print("Answer ",totalSum * draw[-1])
                    exit()
        i+=1

