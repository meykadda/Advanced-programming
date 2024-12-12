amount = float(input("Total amount: "))
nbr = int(input("Number of items: "))
day = str(input("Day of the week: ")).capitalize()
weekday = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
weekend = ['Saturday', 'Sunday']
if day in weekday:
    amount = amount - (amount * 10 / 100)
elif day in weekend:
    amount = amount - (amount * 20 / 100)
else:
    print("Day doesn't exist")
    exit()
if nbr > 5:
    amount = amount - (amount * 5 / 100)
print(f"Total price after discount: {amount} dinars")
