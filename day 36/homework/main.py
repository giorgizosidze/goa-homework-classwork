# 1 davaleba

score = {
    "nia" : 95,
    "giorgi" : 90,
    "luka" : 65
}

for name, grade in score.items():
    print(name, "->", grade)


# 2 davaleba

score.update({
    "nino" : 80,
    "mari" : 60
})

print("score after update:", score)


# 3 davaleba

country = {
    "kai" : "georgia",
    "fr" : "france",
    "it" : "italy"
}

value = country.pop("kai")
country["ge"] = value

print("country after pop:", country)


# 4 davaleba

# update() -> amatebs axal key-value wyvilebs dictionary-si an tu key ukve arsebobs, misi vlue icvleba


# 5 davaleba

# pop(key) -> slis dictionary -dan mititebuli key-s da abrunebs mis values-s


# 6 davaleba

product = {
    "apple" : 3,
    "banana" : 5,
    "milk" : 9
}

print("seiyvane producti: ")

user_product = input("semoiyvane produqti")

if user_product in product:
    print("fasi: ", product[user_product])
else:
    print("aseti produqti ar arsebobs")

product.update({"puri": 4})
print("axali produqtebi:", product)

product.clear()
print("dasuftavebis semdeg:", product)

# 7 davaleba

# celar() -> slis dictionary-s yvela elemnts da tovebs cariel dictionary-s 