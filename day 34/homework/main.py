# 1 davaleba

# ორი tuple
numbers = (1, 2, 3, 4, 5)
colors = ("red", "green", "blue")

# გაერთიანება
combined = numbers + colors

print("ახალი tuple:", combined)


# 2 davaleba

# tuple
fruits = ("apple", "banana", "cherry")

# შემოწმება
if "banana" in fruits:
    print("banana არის tuple-ში")
else:
    print("banana არ არის tuple-ში")


# 3 davaleba

# tuple რიცხვებით
nums = (1, 2, 3, 4, 5, 6, 7, 8)

print("ლუწი რიცხვები:")
for n in nums:
    if n % 2 == 0:   # თუ 2-ზე უნაშთოდ იყოფა
        print(n)


# 4 davaleba


# მოცემული tuple
numbers = (3, 6, 8, 1, 9, 12, 4)

# ქულების counter
score = 0

print("ლუწი რიცხვებია:")
for n in numbers:
    if n % 2 == 0:  # ვამოწმებთ არის თუ არა ლუწი
        print(n)    # დაბეჭდე ლუწი
        score += 1  # თითო ლუწზე ქულას ვამატებთ

print("ჯამში მოიპოვე:", score, "ქულა")


# 5 davaleba

# tuple სიტყვებით
words = ("apple", "banana", "apple", "cherry", "banana", "apple")

# თითოეული სიტყვის დათვლა
for w in set(words):   # set() -> უნიკალური მნიშვნელობები
    count = words.count(w)
    print(f"{w} - {count} ჯერ მეორდება")
