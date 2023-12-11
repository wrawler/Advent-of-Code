file = open("input.txt","r")
lines = file.readlines()

data = []
for line in lines:
    words = line.split()
    
    collection = []
    for word in words:
        if word.isnumeric():
            collection.append(int(word))
    
    data.append(collection)
file.close()
    
TimeMeasurements = data[0]
DistanceMeasurements = data[1]

totalWaysToWin = []
for i in range(len(TimeMeasurements)):
    waysToWin = 0
    for j in range(1,TimeMeasurements[i]):
        if (j * (TimeMeasurements[i] - j)) > DistanceMeasurements[i]:
            print(j,TimeMeasurements[i] - j,j * (TimeMeasurements[i] - i))
            waysToWin += 1
    totalWaysToWin.append(waysToWin)

ans = totalWaysToWin[0]
for i in totalWaysToWin[1:]:
    ans *= i 

print(ans)