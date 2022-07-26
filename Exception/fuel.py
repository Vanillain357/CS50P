while True:
    try:
        x, y = input("Fraction: ").split("/")
        x = int(x)
        y = int(y)
        if (y > 0) and (x <= y):
            break
    except ValueError:
        pass

gague = x / y

if gague <= 0.01:
    print("E")
elif gague >= 0.99:
    print("F")
else:
    print(f"{round(gague*100)}%")