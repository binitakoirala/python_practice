#
# Write a program that asks the user to enter a traffic light color (red, yellow, green) and prints "Stop" for red, "Slow down" for yellow, and "Go" for green.
traffic_color = input("Enter a traffic light color: ").lower()

match traffic_color:
    case "red":
        print("Stop")
    case "yellow":
        print("Slow down")
    case "green":
        print("Go")
    case _:
        print("Invalid color.")
