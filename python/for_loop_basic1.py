# Basic - print all integers from 0 to 150:
print("integers, from 0 to 150")
for i in range(0,151):
    print (i)

#Multiples of Five - print all the multiples of 5 from 5 to 1,000
print ("Multiples of five, from 5 to 1k")
for i in range (0,1001,5):
    print (i)


#Counting, the dojo way
print ("Counting, the dojo way")
for i in range (1,101):
    if i%10==0:
        print ("Coding Dojo")
    elif i%5==0:
        print ("Coding")
    else:
        print (i)


#Whoa.  That sucker's Huge
x=0
for i in range (0,500001):
    if i%2==1:
        x=x+i
print ("Total of odd values from 0-500,000 = "+str(x))

#count by 4s from 2018 to 0
print ("Counting by 4s, from 2018 to 0")
for i in range (2018,0,-4):
    print (i)


#Flexible counters
print ("Flexible counters:")
lowNum=2
highNum=9
mult=3
for i in range (lowNum,(highNum+1)):
    if i%mult==0:
        print (i)




