import sys

# f = text file when opened
f = open(sys.argv[1]).read().split()

# dictionary of hex values and count
hexDict = {}
countDict = {}

# loop through .txt to read and store data
for line in f:
    x = line.lstrip("0") or '0'
    hexDict[int(str(x), base=16)] = x
    if countDict.get(x) < 1:
        countDict[x] = 1
    else:
        countDict[x] += 1

# sort the data by size
sortList = list(hexDict)
sortList = sorted(sortList)

# output Hex value and number of occurrences
for sort in sortList:
    x = int(sort)
    hexValue = hexDict[x]
    if countDict[hexValue] > 1:
        print("%s %s" % (hexValue, countDict[hexValue]))
