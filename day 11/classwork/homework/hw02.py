#2 davaleba


age = int(input("seiyvane sheni asaki "))
has_student_card = input("studentis barati tu gaq?")

if age <18 or has_student_card.lower() == "ki":
    print("danazogi ")
elif age >= 60 and has_student_card.lower() == "ara":
    print("fazdakleba gaq ogond pensioneri")
else:
    print("fazdakleba")