people = int(input("How many people need a ride? "))
taxi = int(input("How many people fit in one taxi? "))
if people > 0:
    if taxi >0:
        rides = (people // taxi)
        if people % taxi != 0:
            rides =rides +1
        print(f"Number of taxis needed: {rides}")
    else:
        print("the number of prople fitting in one taxi must be positive!")
else:
    print("the number of people should be positive!")