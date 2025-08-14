#1 davaleba

def setence_to_comma_list(sentence):
    words = sentence.split()
    result = ",".join(words)
    return result
print(setence_to_comma_list("miyvars programireba"))

# 2 davaleba

def print_word_legeths(sentence):
    words = sentence.split()
    for word in words:
        print(f"{word} - {len(word)} simbolo")



# 3 davaleba


def remove_extra_speaces(sentence):
    words = sentence.split()
    clean_sentence = " ".join(words)
    return clean_sentence
print(remove_extra_speaces("miyvars kodireba"))


# 4 davaleba

def replace_space_with_dash(sentence):
    words = sentence
    dashed = "-".join(words)
    return dashed
print(replace_space_with_dash("miyvars programireba"))


# 5 davaleba


def reverse_words(sentence):
    words = sentence.split()
    reverse_words = words[::-1]
    return " ".join(reverse_words)
print(reverse_words("dges wvima iko"))
























