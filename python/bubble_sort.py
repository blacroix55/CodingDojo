arr=[5,7,8,2,3,1,9,6,0,4]

print ("start =",arr)
# swap=False
bubbleCounter=0
checks=0
while True:
    swap=False
    for i in range(1,len(arr)-bubbleCounter):
        checks=checks+1
        # print (arr[i-1],arr[i])
        if arr[i-1]>arr[i]:
            # print ("swapping")
            arr[i-1],arr[i]=arr[i],arr[i-1]
            swap=True
    bubbleCounter=bubbleCounter+1
    # print (arr)
    if swap==False:
        break
    
print ("end =",arr)
print ("Num of checks =",checks)