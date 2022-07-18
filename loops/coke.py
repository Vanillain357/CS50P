cost = 50
paid = 0
accepted = [5, 10, 25]

while paid < cost:
    print("Amount Due:", cost)
    tender = int(input("Insert Coin: "))
    if tender in accepted:
        cost -= tender

print("Change Owed:", 0 - cost)