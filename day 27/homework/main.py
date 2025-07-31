# 1 davaleba

def remove_first_and_last(a):
    return a[1:-1]
print(remove_first_and_last(["h", "i", "t", "l", "e", "r"]))



# 2 davaleba

def mutliply_sums(list1, list2):
    sum1 = 0
    for num in list1:
        sum1+=num
        
    sum2 = 0
    for num in list2:
        sum2+=num
    return sum1 * sum2
print(mutliply_sums([1, 2, 3, 4, 5],[6, 7]))




# 3 davaleba

def double(L):
    result = []
    i = 0
    while i < len(L):
        result.append(L[i]*2)
        i += 1
    return result
print(double([1, 2, 3]))



# 4 davaleba

def even_number(G):
    even = []
    for num in G:
        if num % 2 == 0:
            even.append(num)
    return even 
print(even_number([1, 2, 3]))




# 5 davaleba

def name(list1):
    index = " ".join(list1)
    list = index.split()
    result = []
    for list1 in list:
        if list1[0] == "N":
            result.append(list1)
    return result
print(name(["Nika", "Giga", "Niga", "Mamuka"]))