def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    import string
    letters = list(string.ascii_uppercase)

    numbers = []
    for i in range(10):
        numbers.append(str(i))

    first_number = False

    if len(s) < 2 or len(s) > 6:
        return False

    if s[0] in letters:
        for character in s:
            if first_number == False:
                if character == "0":
                    return False
                if character in numbers:
                    first_number = True
                if (character not in numbers) and (character not in letters):
                    return False
            else:
                if character not in numbers:
                    return False
    else:
        return False

    return True


main()