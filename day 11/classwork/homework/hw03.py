
#3 davaleba

num1 = int(input("semoiyvane pirveli ricxvi"))
num2 = int(input("meore ricxvi semoiyvane"))

if num1 > 0 and num2 > 0:
    print("yvela dadebiti")
elif(num1 > 0 and num2 <= 0) or (num2 > 0 and num1 <= 0):
    print("dadebiti")
else:
    print("araa dadebiti")