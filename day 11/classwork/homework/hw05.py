
#5 davaleba

a = 1
b = 0
c = 0

result_0 = (a and not b) or (b and not a)
result_1 = (b and c) and (a or b)
result_2 = (a and not c) or (b and not a) or (b and not c)

print("Result 0:",result_0)
print("Result 1:",result_1)
print("Reslut 2:",result_2)
