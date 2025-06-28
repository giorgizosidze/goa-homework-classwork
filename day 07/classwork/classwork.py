# 1 davaleba

while True: 
    print(1)
    break

# 2 davaleba

name = input("enter your a name")

i = 0
while i <10:
    print(name)
    i += 1

# 3 davaleba

number = int(input("enter a number: "))
while number <= 100:
    number = int(input("the number must be more than 100 try again: "))
print("thank you the number you gave me indeed more than 100:", number)

# 4 davaleba

names = ""
i = 0

while i < 5:
    name = input("enter your name: ")
    if i == 0:
        names = name
    else:
        names += ", " + name
    i += 1

print("you entered this names: ", names)