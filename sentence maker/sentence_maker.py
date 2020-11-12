def sentence_maker(phrase):
    interogative = ("how" , "what" , "why")
    capatlizes = phrase.capitalize()
    if phrase.startswith(interogative):
        return("{}?".format(capatlizes))

    else:
        return("{}.".format(capatlizes))

result = []
while True:
    user = input("Enter something: ")

    if user == "\end":
        break

    else:
        result.append(sentence_maker(user))

print(" ".join(result))