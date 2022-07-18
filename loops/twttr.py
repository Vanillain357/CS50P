vowels = ["a", "e", "i", "o", "u"]
out_string = ""

twttr = input("Input: ")

for character in twttr:
    if character.lower() not in vowels:
        out_string += character

print("Output:", out_string)