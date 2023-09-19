
num_floors = 16
current_floor = 0
def move_elevator(target_floor):
    global current_floor
    if 0 <= target_floor < num_floors:
        current_floor = target_floor
        display_floors(current_floor)
    else:
        print("Invalid floor request")
        
def display_floors(current):
    for floor in range(num_floors):
        if floor == current:
            print(f"{floor} - You are here")
        else:
            print(floor)
while True:
    print("\nCurrent Floor:", current_floor)
    target_floor = int(input("Enter target floor (0 to 15) or -1 to exit: "))
    if target_floor == -1:
        break
    move_elevator(target_floor)

print("Elevator program has ended.")