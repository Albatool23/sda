
# Biggie Size
def Biggie_Size (x:list):
    for j in range(0,len(x)):
        if x[j] > 0:
            x[j] = "big"
    return x

print (Biggie_Size([-1,2,4,7]))


# Count Positives
def Count_Positives (x:list):
    count = 0
    for j in x:
        if j > 0:
            count = count + 1
    x[-1] = count
    return x


print(Count_Positives([-1,2,4,7]))

# Sum Total
def Sum_Total (x:list):
     j = sum(x)
     print(x)

print (sum([1,2,4,7]))

# Average
def Average (x:list):
    avg = sum(x) / len(x)
    return avg

print(Average([1,2,4]))

# Length
def Length(x:list):
    j = len(x)

print(len([[1,2,4]]))


# Minimum
def Minimum (x:list):
    if len(x) == 0 :
        return False

print(min([8,2,4,7]))

# Maximum
def Maximum (x:list):
    if len(x) >= 0 :
        return False

print(max([8,2,4,7]))


# Ultimate Analysis
def Ultimate_Analysis (x:list):
    avg = sum(x) / len(x)
    return avg
    len(x)
    max(x)
    min(x)
print(Ultimate_Analysis([5,9,2,4,6]))
print(len([5,9,2,4,6]))
print(max([5,9,2,4,6]))
print(min([5,9,2,4,6]))


# Reverse List
def Reverse_List (x:list):
    new_lst = x[::-1]
    return new_lst

print(Reverse_List([5,9,2,4,6]))


