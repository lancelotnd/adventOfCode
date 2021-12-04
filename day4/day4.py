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

lines.pop(0)
master = []
i = 0
bigString = ''
for l in lines:
    bigString += l

bigString = bigString.replace('\n', '')
bigString = bigString.split()

results = list(map(int, bigString))

x = 25
list_of_lists = [results[i: i + x]
                 for i in range(0, len(results), x)
                 ]
allNumbers = [int(x) for x in allNumbers]
draw = []
i = 1
noWinner = True
toTest = []

while(noWinner):
    for i in range(len(allNumbers)):
        toTest = allNumbers[0:i]
        for l in list_of_lists:
            for j in toTest:
                if(int(j) in l):
                    noWinner =  isWinning(l, toTest)
                    if isWinning(l, toTest):
                        noWinner = False
                        print(toTest, l)
                        print("winner")

                        exit()
                
    i+=1

  
