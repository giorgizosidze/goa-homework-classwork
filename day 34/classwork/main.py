# 1 davaleba
fruits = ("მსხალი", "ვაშლი", "მარწყვი", "ალუბალი", "ატამი")
print(fruits[0])
print(fruits[2])
print(fruits[-1])

# 2 davaleba
fruits = ("მსხალი", "ვაშლი", "მარწყვი", "ალუბალი", "ატამი")
t = list(fruits)
t[2] = "ვაშლატამა"
fruits = tuple(t)
print(fruits)

# 3 davaleba
A = (1,2,3,4)
B = (6,7,8)
print(A + B)
print(A * 2)

# 4 davalenba
tuple = (1,2,3,4,5,6,6,6,67,8)
print(tuple.index(67))
print(tuple.count(6))