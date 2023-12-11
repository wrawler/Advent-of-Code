file = open("input2.txt","r")
lines = file.readlines()

data = []
for line in lines:
    words = line.split()
    
    collection = ""
    for word in words:
        if word.isnumeric():
            collection += word
    
    data.append(collection)
file.close()
    
TimeMeasurement = int(data[0])
DistanceMeasurement = int(data[1])

totalWaysToWin = []
waysToWin = 0
for j in range(1,TimeMeasurement):
    if (j * (TimeMeasurement - j)) > DistanceMeasurement:
        waysToWin += 1

ans = waysToWin
print(ans)