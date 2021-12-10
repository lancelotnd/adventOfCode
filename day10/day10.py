with open('input.txt') as f:
    lines = f.readlines()

m = [l.replace('\n', '') for l in lines]    

openingElements = ["(","[","{","<"]
closingElements = [")","]","}",">"]
pointsPerChar = {")":3, "]":57,"}":1197,">":25137}
totalPoints = 0
openingPile = []
err = []
for r in m:
    for c in r:
        if(c in openingElements):
            openingPile.insert(0, c)
        elif openingPile[0] == openingElements[closingElements.index(c)]:
            openingPile.pop(0)
        else:
            err.append(str(r + "  - Expected "+ closingElements[openingElements.index(openingPile[0])]+ " but found "+ c+ " instead."))
            totalPoints += pointsPerChar[c]
            break
for e in err:
    print(e)
print("answer: ", totalPoints)            