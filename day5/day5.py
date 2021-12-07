with open('input.txt') as f:
    lines = f.readlines()

def missing_point_1d(p1, p2):
    toReturn = []
    if p1 < p2:
        toReturn.append(p1)
        while(p1 + 1 < p2):
            p1 += 1
            toReturn.append(p1)
        toReturn.append(p2)
    else:
        toReturn.append(p1)
        while(p1 - 1 > p2):
            p1 -= 1
            toReturn.append(p1)
        toReturn.append(p2)
    return toReturn




def generate_missing_points(coord):
    index = 0
    target = 10000000000000
    isDiag = (coord[0][1] != coord[1][1]) and (coord[0][0] != coord[1][0])
    isX = coord[0][1] == coord[1][1] #is it X that change

    if isDiag:
        x1 = coord[0][0]
        y1 = coord[0][1]
        x2 = coord[1][0]
        y2 = coord[1][1]

        x = missing_point_1d(x1, x2)
        y = missing_point_1d(y1, y2)

        toReturn = []
        for i in range(len(x)):
            toReturn.append([x[i], y[i]])

        
    elif(isX):
        if coord[0][0] < coord[1][0]:
            toReturn = []
            toReturn.append(coord[0])
            other  = coord[0][1]
            target = coord[1][0]
            index = coord[0][0]
            while(index+1 < target):
                index += 1
                toReturn.append([index, other])
            toReturn.append(coord[1])
        else:
            toReturn = []
            toReturn.append(coord[0])
            other  = coord[0][1]
            target = coord[1][0]
            index = coord[0][0]
            while(index-1 > target):
                index -= 1
                toReturn.append([index, other])
            toReturn.append(coord[1])
    else:
         if coord[0][1] < coord[1][1]:
            toReturn = []
            toReturn.append(coord[0])
            other  = coord[0][0]
            target = coord[1][1]
            index = coord[0][1]
            while(index+1 < target):
                index += 1
                toReturn.append([other, index])
            toReturn.append(coord[1])
         else:
            toReturn = []
            toReturn.append(coord[0])
            other  = coord[0][0]
            target = coord[1][1]
            index = coord[0][1]
            while(index-1 > target):
                index -= 1
                toReturn.append([other, index])
            toReturn.append(coord[1])
    return toReturn
    

master = []
for l in lines:
    l = l.replace("\n", '')
    a = l.split(" -> ")
    mini = []
    for e in a:
        w = e.split(',')
        w = [int(x) for x in w]
        mini.append(w)
    master.append(mini)

purged = []


dictP = {}

for l in master:
    m = generate_missing_points(l)
    for n in m:
      s = str(n)
      if s not in dictP:
          dictP[s] = 0
      dictP[s] += 1

pointsCrossing = 0

for k in dictP:
    if dictP[k] > 1:
        pointsCrossing += 1

print("Answer points crossing: ", pointsCrossing)





        

                

