file = open("input.txt","r")
ans = 0

for line in file:
    firstDigit = None
    lastDigit = None
    joined = None
            
    for character in line:
        if character.isdigit() and firstDigit is None:
            firstDigit = character
            lastDigit = character
        
        elif character.isdigit():
            lastDigit = character
    
    if firstDigit is not None and lastDigit is not None:
        joined = firstDigit + lastDigit
        ans += int(joined)

file.close()
print(ans)