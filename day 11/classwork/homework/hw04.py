
#4 davaleba

num1 = int(input("seiyvane ricxvi"))
num2 = int(input("seiyvane meore ricxvi"))
operacia = input("seiyvane sxva operaciebi rogoricaa: (+, -, *, /)")

if operacia == "+":
    print(num1 + num2)
elif operacia == "-":
    print(num1 - num2)
elif operacia == "*":
    print(num1 * num2)
elif operacia == "/":
    if num2  != 0:
        print(num1 / num2)
    else:
        print("araa swori")
else:
    print("araa zma swori")