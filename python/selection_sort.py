arr=[5,7,8,2,3,1,9,6,0,4]

print ("start =",arr)

for workingPosition in range(0,len(arr)):
    lowestPosition=workingPosition
    for comparisonValue in range(workingPosition,len(arr)):
        if arr[comparisonValue]<arr[lowestPosition]:
            lowestPosition=comparisonValue
    if lowestPosition!=workingPosition:
        arr[workingPosition],arr[lowestPosition]=arr[lowestPosition],arr[workingPosition]
    print ("Pass number",workingPosition)
    print ("current array = ",arr)

print ("end =",arr)
