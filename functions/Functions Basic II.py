
# Countdown
def count (x:int):
    list1 = []
    for j in range(x,-1,-1):
        list1.append(j)
    return list1

print(count(5))


# Print and Return
def printAndReturn (x:list):
    print(x[0])
    return x[1]

print(printAndReturn([4,7]))


# first_plus_length
def first_plus_length (x:list):
    return x[0] + len(x)

print(first_plus_length([1,2,5,6]))

# values_greater_than_second [1,2,4,6]
def values_greater_than_second(x:list):
    if len(x) < 2 :
        return False
    list2 = []
    for j in x:
        if x[1] < j:
            list2.append(j)
    return list2

print(values_greater_than_second([1,2,3,4,5]))

# length_and_value
def length_and_value (x:int,y:int):
    return x*[y]

print(length_and_value(5,3))




