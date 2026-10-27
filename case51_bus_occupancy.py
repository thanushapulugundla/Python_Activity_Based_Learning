capacity = int(input("Enter bus capacity: "))
stops = int(input("Enter number of stops: "))
passengers = 0
if capacity <= 0 or stops <= 0:
    print("Invalid capacity or number of stops")
else:
    for i in range(stops):
        print("Stop", i + 1)
        boarding = int(input("Passengers boarding: "))
        alighting = int(input("Passengers alighting: "))
        if boarding < 0 or alighting < 0 or alighting > passengers:
            print("Invalid passenger details")
            continue
        passengers = passengers - alighting + boarding
        print("Current passengers:", passengers)
        if passengers > capacity:
            print("Capacity exceeded")
    print("Final passenger count:", passengers)