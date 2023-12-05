file = open("input.txt","r")
lines = file.readlines()
ans = 0

gameNumber = 1
for line in lines:
    gameValid = True
    line = line.replace(";"," ")
    line = line.replace(","," ")
    words = line.split()
    
    numberOfCubes = 0
    for word in words:
        if word.isnumeric():
            numberOfCubes = int(word)
        
        elif word in ["red","green","blue"]:
            if  (word == "red" and numberOfCubes > 12) or\
                (word == "green" and numberOfCubes > 13) or\
                (word == "blue" and numberOfCubes > 14):
                    gameValid = False
    
    if gameValid == True:
        print(gameNumber)
        ans += gameNumber

    gameNumber += 1

file.close()
print(ans)