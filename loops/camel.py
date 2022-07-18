camel = input("camleCase: ")
out_string = ""

for character in camel:
    if character.isupper():
        out_string += "_" + character.lower()
    else:
        out_string += character

print("snake_case:", out_string)