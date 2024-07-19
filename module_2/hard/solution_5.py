#
# Write a program that asks the user to enter a mode of transportation (car, bus, bike, walk) and prints the average speed using a match-case statement.
transportation_mode = input("Enter a mode of transportation: ").lower()

match transportation_mode:
    case "car":
        print("Urban: 15-30 km/h\nHighway: 80-120 km/h")
    case "bus":
        print("Urban: 15-25 km/h\nHighway: 60-80 km/h")
    case "bike":
        print("Beginner: 16-19 km/h\nExperienced: 24-29 km/h")
    case "walk":
        print("3-5 km/h")
