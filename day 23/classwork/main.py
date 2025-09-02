user_input = input("gtxovt semoiyvane nebismieri sityva romelic iwyeba da mtavrdeba tanxmovanze: ")


letters = "a e i o u"

while True:
    if user_input[0] in letters or user_input[-1] in letters:
        user_input = input("arasworia gtxovt semoiyvanot tavidan: ")
    else:
        print(user_input + "sworia da gmadlobt")
        break