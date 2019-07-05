
    # Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
    #     Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]
def biggie_size(l):
    for i in range(0,len(l)):
        if l[i]>0:
            l[i]="big"
    return l
print ( biggie_size([-1, 3, 5, -5]) )
    
    # Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. (Note that zero is not considered to be a positive number).
    #     Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
    #     Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it
def count_positives(l):
    c=0
    for i in range(0,len(l)):
        if l[i]>0:
            c=c+1
    l[len(l)-1]=c
    return l
print( count_positives([-1,1,1,1]) )             # [-1,1,1,3] 
print( count_positives([1,6,-4,-2,-7,-2]) )      # [1,6,-4,-2,-7,2]

   
    # Sum Total - Create a function that takes a list and returns the sum of all the values in the array.
    #     Example: sum_total([1,2,3,4]) should return 10
    #     Example: sum_total([6,3,-2]) should return 7
def sum_total(l):
    sum=0
    for i in range(0,len(l)):
        sum=sum+l[i]
    return sum
print( sum_total([1,2,3,4]) ) # 10
print( sum_total([6,3,-2]) ) # 7
 
 
    # Average - Create a function that takes a list and returns the average of all the values.
    #     Example: average([1,2,3,4]) should return 2.5
def average(l):
    c=0
    sum=0
    for i in range(0,len(l)):
        sum=sum+l[i]
        c=c+1
    return sum/c
print(average([1,2,3,4]))  # 2.5
 
 
    # Length - Create a function that takes a list and returns the length of the list.
    #     Example: length([37,2,1,-9]) should return 4
    #     Example: length([]) should return 0
def length(l):
    return len(l)

print( length([37,2,1,-9]) ) # 4
print( length([]) ) # 0

  
    # Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
    #     Example: minimum([37,2,1,-9]) should return -9
    #     Example: minimum([]) should return False
def minimum(l):
    if len(l)==0:
        return False
    lowNum=0
    for i in range(0,len(l)):
        if l[i]<lowNum:
            lowNum=l[i]
    return lowNum
print( minimum([37,2,1,-9]) ) # -9
print(minimum([])) # false



    # Maximum - Create a function that takes a list and returns the maximum value in the array. If the list is empty, have the function return False.
    #     Example: maximum([37,2,1,-9]) should return 37
    #     Example: maximum([]) should return False
def maximum(l):
    if len(l)==0:
        return False
    highNum=0
    for i in range(0,len(l)):
        if l[i]>highNum:
            highNum=l[i]
    return highNum
print( maximum([37,2,1,-9]) ) # 37
print( maximum([]) ) # false

    # Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.
    #     Example: ultimate_analysis([37,2,1,-9]) should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }
def ultimate_analysis(l):
    sumTotal=0
    minimum = l[0]
    maximum = l[0]
    length = len(l)
    for i in range(0,length):
        if l[i]<minimum:
            minimum=l[i]
        if l[i]>maximum:
            maximum=l[i]
        sumTotal=sumTotal+l[i]
    average=sumTotal/length
    myDict={'sumTotal':sumTotal, 'average': average ,'minimum': minimum, 'maximum':maximum,'length': length}
    return myDict
print( ultimate_analysis([37,2,1,-9]) ) 

    # Reverse List - Create a function that takes a list and return that list with values reversed. Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)
    #     Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]
def reverse_list(l):
    newList=[]
    for i in range(len(l)-1,-1,-1):
        newList=newList+[l[i]]
    return newList
print ( reverse_list([37,2,1,-9] ) )
