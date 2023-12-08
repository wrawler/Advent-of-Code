ans = 0

file = open("input2.txt","r")
lines = file.readlines()
numbers = []

lineNumber = 0
for line in lines:
    characterIndex = 0

    numbersToCheck = []
    for character in line:
        if character == "*":
            # Getting all the neighbour characters
            top         = lines[lineNumber - 1][characterIndex]      if lineNumber > 0                                                 else ""
            bottom      = lines[lineNumber + 1][characterIndex]      if lineNumber < len(lines) - 1                                    else ""
            left        = line[characterIndex - 1]                  if characterIndex > 0                                            else ""
            right       = line[characterIndex + 1]                  if characterIndex < len(line) - 1                                else ""
            topLeft     = lines[lineNumber - 1][characterIndex - 1]  if lineNumber > 0 and characterIndex > 0                          else ""
            topRight    = lines[lineNumber - 1][characterIndex + 1]  if lineNumber > 0 and characterIndex < len(line) - 1              else ""
            bottomLeft  = lines[lineNumber + 1][characterIndex - 1]  if lineNumber < len(lines) - 1 and characterIndex > 0             else ""
            bottomRight = lines[lineNumber + 1][characterIndex + 1]  if lineNumber < len(lines) - 1 and characterIndex < len(line) - 1 else ""

            print("Neighbours found: ",top,bottom,left,right,topLeft,topRight,bottomLeft,bottomRight)
            
            # Getting the indices of any digits close to "*"
            if top.isdigit():
                numbersToCheck.append([lineNumber - 1,characterIndex])
            
            if bottom.isdigit():
                numbersToCheck.append([lineNumber + 1,characterIndex])
            
            if left.isdigit():
                numbersToCheck.append([lineNumber,characterIndex - 1])
            
            if right.isdigit():
                numbersToCheck.append([lineNumber,characterIndex + 1])
            
            if topLeft.isdigit():
                numbersToCheck.append([lineNumber - 1,characterIndex - 1])
            
            if topRight.isdigit():
                numbersToCheck.append([lineNumber - 1,characterIndex + 1])
            
            if bottomLeft.isdigit():
                numbersToCheck.append([lineNumber + 1,characterIndex - 1])
            
            if bottomRight.isdigit():
                numbersToCheck.append([lineNumber + 1,characterIndex + 1])

            print("Found Numbers to check")
            
        # Extracting the numbers close to "*"
        for index in numbersToCheck:
            number = ""
            
            leftMostDigitFound = False
            rightMostDigitFound = False
            numberIncomplete = True
            lineIndex = index[0]
            charNearGearIndex = index[1]
            
            leftIndex = 1
            rightIndex = 1
            
            while numberIncomplete:
                leftCharacter = charNearGearIndex - leftIndex
                rightCharacter = charNearGearIndex + rightIndex
                
                if lines[lineIndex][leftCharacter - leftIndex].isdigit():
                    number = lines[lineIndex][leftCharacter - leftIndex] + number
                    leftIndex += 1
                    
                else:
                    leftMostDigitFound = True    
                        
                if lines[lineIndex][leftCharacter + rightIndex].isdigit():
                    number = number + lines[lineIndex][leftCharacter + rightIndex]
                    rightIndex += 1
                    
                else:
                    rightMostDigitFound = True
                
                if leftMostDigitFound and rightMostDigitFound:
                    print("number found")
                    print(number)
                    
                    numberIncomplete = False
            
            numbers.append(int(number))
            number = ""
        characterIndex += 1
    lineNumber += 1
        
file.close()
# for i in numbers:
#     print(i)