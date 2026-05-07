# Implement a program that prompts the user to insert a coin, one at a time, each time informing the user of the amount due. Once the user has inputed at least 50 cents, output how many coins in change the user is owed. Assume that the user will only input integers, and ignore any integer that isn't an accepted denomination.
# Accepted denominations: 25 cents, 10 cents and 5 cents.

amount_due = 0
coin = 0

while amount_due < 50:
    coin = int(input("Insert coin: "))
    
    if coin == 5 or coin == 10 or coin == 25:
        amount_due += coin
        print(f"Amount due: {50 - amount_due}")
    else:
        print(f"Amount due: {50 - amount_due}")

change = amount_due % 50
print(f"Change owed: {change}")
