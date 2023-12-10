ans = 0

seeds = []
sources = {}

# Loading data from file
file = open("input.txt","r")
lines = file.read().split("\n\n")

seperatedData = {}
for line in lines:
    heading = line.split("\n")[0].replace(":","")
    seperatedData[heading] = line.split("\n")[1:] # getting the data AFTER the heading as value
    
file.close()

# Getting the seeds
seedsString = next(iter(seperatedData.keys())).split()[1:]
seeds = list(int(seed) for seed in seedsString)

# Removed the first element from seperatedData, it had the seeds but in bad format
firstKey = list(seperatedData.keys())[0]
del seperatedData[firstKey]
sources = seperatedData

for convertionRanges in seperatedData.values():
    
    # Convert the data from string to lists
    convertionRanges = [[int(number) for number in convertionRange.split(" ") if number] for convertionRange in convertionRanges]
    
    seedIndex = 0
    for seed in seeds:
        mapped = False
        
        for convertionRange in convertionRanges:
            
            destinationRangeStart = convertionRange[0]
            sourceRangeStart = convertionRange[1]
            rangeLength = convertionRange[2]
            
            if sourceRangeStart > destinationRangeStart:
                difference = sourceRangeStart - destinationRangeStart
            
            elif sourceRangeStart < destinationRangeStart:
                difference = destinationRangeStart - sourceRangeStart
            
            if seed >= sourceRangeStart and seed <= sourceRangeStart + rangeLength:
                if not mapped:
                    if  sourceRangeStart > destinationRangeStart:
                        seeds[seedIndex] = seed - difference
                    
                    elif sourceRangeStart < destinationRangeStart:
                        seeds[seedIndex] = seed + difference
                
                    else:
                        seeds[seedIndex] = seed
                
                    mapped = True
        
        seedIndex += 1

lowestLocation = seeds[0]
for seed in seeds:
    if seed < lowestLocation:
        lowestLocation = seed

ans = lowestLocation
print(ans)