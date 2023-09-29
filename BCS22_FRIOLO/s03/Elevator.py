import time

def elevator_simulation(total_floors):
    current_floor = 1

    while True:
        print(f"You are at the floor: {current_floor}")

        target_floor = input("Enter target floor (1 to 15) or 'q' to quit: ")

        if target_floor == 'q':
            print("End progress!")
            break

        try:
            target_floor = int(target_floor)
            if 1 <= target_floor <= total_floors:
                if target_floor > current_floor:
                    for floor in range(current_floor + 1, target_floor + 1):
                        print(floor)
                        time.sleep(1)
                elif target_floor < current_floor:
                    for floor in range(current_floor - 1, target_floor - 1, -1):
                        print(floor)
                        time.sleep(1)
                current_floor = target_floor
            else:
                print("Invalid floor number. Please enter a floor between 1 and 15.")
        except ValueError:
            print("Invalid input. Please enter a valid floor number or 'q' to quit.")

if __name__ == "__main__":
    total_floors = 15
    print("Elevator Simulation")
    elevator_simulation(total_floors)