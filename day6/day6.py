with open('input.txt') as f:
    lines = f.readlines()

m = lines[0].split(',')
m = [int(x) for x in m]

d = {}
for e in m:
    if str(e) not in d:
        d[str(e)] = 0
    d[str(e)] += 1    

for i in range(256):
   tmp = {"0":0, "1":0, "2":0, "3":0, "4":0, "5":0, "6":0, "7":0, "8":0, }
   for k in d:
        if(int(k) == 0):
            tmp[str(6)] += d[k] 
            tmp[str(8)] += d[k]
        else:

            tmp[str(int(k)-1)] += d[k]

   d = tmp
   print(d)
   total = 0
   for k in d:
       total+= d[k]
print("Result number of fishes :",total)

