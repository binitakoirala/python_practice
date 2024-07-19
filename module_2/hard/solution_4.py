#
# Write a program that asks the user to enter a traffic light color (red, yellow, green) and prints the corresponding action (stop, slow down, go) using a match-case statement.
traffic_light_color = input("Enter a traffic light color name: ").lower()

match traffic_light_color:
    case "red":
        print("Stop.")
    case "yellow":
        print("Slow down.")
    case "green":
        print("Go.")
    case _:
        print("Invalid color.")
