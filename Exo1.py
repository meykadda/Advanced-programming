TICKET= 15.5
name=string=(input("Please enter your name : "))
if name=="VIP":
    print("Enjoy the show for free!")
else:
    nbr=int(input("How many tickets would you like to buy? "))
    cost= nbr * TICKET
    print(f"The total cost is :{cost} ")
    print("Enjoy your tickets!")
