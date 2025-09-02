# 1 davaleba

word = input("semoiyvane sityva")

if len(word) > 5:
    print(word.lower())
else:
    print(word.upper())
    
# 2 davaleba

def func(word, letter):
    return word.find(letter)

print(func("programireba", "p"))
print(func("goa", "g"))

def func(word,letter) :
    return word.lower().find(letter.lower())


    
