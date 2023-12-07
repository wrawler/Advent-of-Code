ans = 0

def isSymbol(character):
    # Check if the character is ASCII and not alphanumeric
    return character.isascii() and not character.isalnum() and not character == "." and not character == "\n"

file = open("input2.txt","r")
lines = file.readlines()

lineIndex = 0
for line in lines:
    validNumber = False
    characterIndex = 0
    number = ""

    for character in line:
        if character.isdigit():

            # Getting all the neighbour characters
            top         = lines[lineIndex - 1][characterIndex]      if lineIndex > 0                                                 else ""
            bottom      = lines[lineIndex + 1][characterIndex]      if lineIndex < len(lines) - 1                                    else ""
            left        = line[characterIndex - 1]                  if characterIndex > 0                                            else ""
            right       = line[characterIndex + 1]                  if characterIndex < len(line) - 1                                else ""
            topLeft     = lines[lineIndex - 1][characterIndex - 1]  if lineIndex > 0 and characterIndex > 0                          else ""
            topRight    = lines[lineIndex - 1][characterIndex + 1]  if lineIndex > 0 and characterIndex < len(line) - 1              else ""
            bottomLeft  = lines[lineIndex + 1][characterIndex - 1]  if lineIndex < len(lines) - 1 and characterIndex > 0             else ""
            bottomRight = lines[lineIndex + 1][characterIndex + 1]  if lineIndex < len(lines) - 1 and characterIndex < len(line) - 1 else ""

            # Getting a valid part(the number with a neighbour symbol)
            if any(isSymbol(neighbour) for neighbour in [top, bottom, left, right, topLeft, topRight, bottomLeft, bottomRight]):
                validNumber = True

            # Checking if their is a digit after this one OR this is the last character in line THEN a number will be finalised
            if (line[characterIndex + 1].isdigit() == False) or (characterIndex == len(line) - 1):
                number += character
                # If finalised number is valid then add it to the answer
                if validNumber == True:
                    print(number)
                    ans += int(number)

                # Reset the number container and the valid flag
                number = ""
                validNumber = False

            # If not then this digit will be concatenated to the number and loop continues
            else:
                number += character

        characterIndex += 1
    lineIndex += 1

file.close()
print(ans)
    
