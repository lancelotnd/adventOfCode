with open('input.txt') as f:
    lines = f.readlines()

m = [l.replace('\n', '') for l in lines]    

openingElements = ["(","[","{","<"]
closingElements = [")","]","}",">"]
pointsPerChar = {")":3, "]":57,"}":1197,">":25137}
pointsAutoComplete = {")":1, "]":2,"}":3,">":4}
totalPoints = 0
err = []

def getClosingChar(openingChar):
    return  closingElements[openingElements.index(openingChar)]

def computeAutoCompleteScore(line):
    score = 0
    for char in line:
        score *= 5
        score += pointsAutoComplete[char]
    return score

validLines = []
scoresAutoComplete = []
for r in m:
    openingPile = []
    wasError = False
    for c in r:
        if(c in openingElements):
            openingPile.insert(0, c)
        elif openingPile[0] == openingElements[closingElements.index(c)]:
            openingPile.pop(0)
        else:
            err.append(str(r + "  - Expected "+ closingElements[openingElements.index(openingPile[0])]+ " but found "+ c+ " instead."))
            totalPoints += pointsPerChar[c]
            wasError = True
            break
    if not wasError:
        validLines.append(r)
        if len(openingPile) != 0:
            complete = ""
            for e in openingPile:
                complete += getClosingChar(e)
            scoresAutoComplete.append(computeAutoCompleteScore(complete))
            #print(complete, " - ", scoresAutoComplete[-1])
        wasError = False
scoresAutoComplete.sort()
print("Answer is : ", scoresAutoComplete[int((len(scoresAutoComplete)-1)/2)])
