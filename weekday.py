d = int(input("input nember (1-7): "))
weekday = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
for i in range(len(weekday)):
    print(weekday[i])
print("_"*20)
for day in  weekday:
    print(day)
print("_"*20)
print(f"day {d}th is {weekday[d-1]}")