
# 1 Update Values in Dictionaries and Lists

# x = [ [5,2,3], [15,8,9] ]
# students = [
#     {'first_name':  'Michael', 'last_name' : 'Bryant'},
#     {'first_name' : 'John', 'last_name' : 'Rosales'}
# ]
# sports_directory = {
#     'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer' : ['Andres', 'Ronaldo', 'Rooney']
# }
# z = [ {'x': 10, 'y': 30} ]


#
# students = [
#     {'first_name':  'Michael', 'last_name' : 'Jordan'},
#     {'first_name' : 'John', 'last_name' : 'Rosales'},
#     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#     {'first_name' : 'KB', 'last_name' : 'Tonel'}
# ]
# def iterateDictionary(list):
#     for dict in list:
#         print (" first_name - {}, last_name - {}".format( dict["first_name"], dict["last_name"]))
#
#
# iterateDictionary(students)
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel





# def iterateDictionary2(key_name, list):
#     for dict in list:
#         print(dict[key_name])
#
# iterateDictionary2('first_name', students)
# iterateDictionary2('last_name' , students)


dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(dict1:dict):
    keys= dict1.keys()
    for key in keys:
       list = dict1[key]
       print(len(list), key)
       for x in list:
           print(x)
       print("")
printInfo(dojo)












