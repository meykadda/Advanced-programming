
name1 = input("Runner 1:\nName: ")
time1 = float(input("Time (in seconds): "))

name2 = input("Runner 2:\nName: ")
time2 = float(input("Time (in seconds): "))

if time1 < time2:
    print(f"The faster runner is {name1}")
elif time2 < time1:
    print(f"The faster runner is {name2}")
else:
    print(f"{name1} and {name2} have the same time")
