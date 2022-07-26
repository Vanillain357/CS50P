month_verbose = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    date = input("Date: ").strip().split(" ")
    if (date[0].title() in month_verbose) and (date[1][-1] == ","):
        try:
            try:
                day = int(date[1].strip(","))
                month = int(month_verbose.index(date[0].title()) +1)
                year = int(date[2])
                if day <= 31 and month <= 12:
                    print(f"{year}-{month:02}-{day:02}")
                    break
            except ValueError:
                pass
        except IndexError:
            pass
    else:
        try:
            month, day, year = date[0].split("/")
            day = int(day)
            month = int(month)
            year = int(year)
            if day <= 31 and month <= 12:
                print(f"{year}-{month:02}-{day:02}")
                break
        except ValueError:
            pass