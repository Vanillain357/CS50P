def main():
    time = convert(input("What time is it? ").strip())

    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")


def convert(time):
    if time[-1] != "m":
        hour, minutes = time.split(":")
        return float(hour) + float(minutes)/60

    else:
        dozen, am_pm = time.split(" ")
        if am_pm == "am":
            return convert(dozen)
        elif am_pm == "pm":
            return convert(dozen) + 12


if __name__ == "__main__":
    main()