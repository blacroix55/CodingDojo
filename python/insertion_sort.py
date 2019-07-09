arr=[6,5,2,3,7,8,9,0,1,4,50,40,10,10,40,3]

def insertionSort(curIndex):
    valToSort=arr[curIndex]  # placeholder for the value being sorted
    for compareIndex in range(curIndex-1,-1,-1):
        if valToSort<arr[compareIndex]:
            arr[compareIndex+1]=arr[compareIndex]
        else:
            compareIndex=compareIndex+1
            break
    arr[compareIndex]=valToSort

print ("starting array =",arr)
for curIndex in range(1,len(arr)):
    insertionSort(curIndex)
print ("final array =",arr)

