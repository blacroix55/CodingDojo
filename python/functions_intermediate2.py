# x = [ [5,2,3], [10,8,9] ] 
# students = [
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'}
# ]
# sports_directory = {
#     'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer' : ['Messi', 'Ronaldo', 'Rooney']
# }
# z = [ {'x': 10, 'y': 20} ]

# Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
# def updateNums(n):
#     if n==10:
#         return 15
#     return n

# for i in range(0,len(x)):
#     for j in range(0,len(x[i])):
#         x[i][j]=updateNums(x[i][j])
# print (x)

# # Change the last_name of the first student from 'Jordan' to 'Bryant'
# def updateName(last):
#     if last == "Jordan":
#         return "Bryant"
#     return last

# for i in range(0,len(x)):
#     students[i]['last_name']=updateName(students[i]['last_name'])
# print (students)

# # In the sports_directory, change 'Messi' to 'Andres'
# def updateName2(last):
#     if last == "Messi":
#         return "Andres"
#     return last

# for sport in sports_directory:
#     for i in range(0,len(sports_directory[sport])):
#         sports_directory[sport][i]=updateName2(sports_directory[sport][i])
# print (sports_directory)
 
# Change the value 20 in z to 30
# def updateNums2(n):
#     if n==20:
#         return 30
#     return n

# for i in z:
#     for v in i:
#         i[v]=updateNums2(i[v])
# print (z)

# students = [
#          {'first_name':  'Michael', 'last_name' : 'Jordan'},
#          {'first_name' : 'John', 'last_name' : 'Rosales'},
#          {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#          {'first_name' : 'KB', 'last_name' : 'Tonel'}
#     ]
# def iterateDictionary(students):
#     for student in students:
#         # keys=(student.keys())
#         for key in student.keys():
#             if key=="first_name":
#                 msg=(key)+" - "+student[key]+", "
#             else:
#                 msg=msg+(key)+" - "+student[key]
#         print (msg)

# iterateDictionary(students)

# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

# def iterateDictionary2(key_name, some_list):
#     for student in some_list:
#         print (student[key_name])

# iterateDictionary2('first_name',students)
# iterateDictionary2('last_name', students)


dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(some_dict):
    for key in some_dict:
        msg="\n"
        count=0
        for some_list in some_dict[key]:
            # print (some_list)
            msg=msg+(some_list)+"\n"
            count=count+1
        print (count,key.upper(),msg)

printInfo(dojo)

# # output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank
    
# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon