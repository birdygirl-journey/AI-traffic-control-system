import random
import time

# Simulated traffic lights
roads = ["North", "South", "East", "West"]

def get_traffic_data():
    """
    Simulate number of cars on each road
    """
    traffic = {}
    for road in roads:
        traffic[road] = random.randint(0, 50)
    return traffic

def choose_green_light(traffic):
    """
    Choose road with maximum traffic
    """
    max_road = max(traffic, key=traffic.get)
    return max_road

def traffic_control_system():
    print("AI Traffic Control System Started...\n")

    for cycle in range(5):
        print(f"--- Traffic Cycle {cycle + 1} ---")

        traffic = get_traffic_data()
        for road, cars in traffic.items():
            print(f"{road} Road: {cars} cars")

        green_road = choose_green_light(traffic)

        print(f"\nGREEN light → {green_road} Road 🚦")
        print("Other roads → RED light ❌\n")

        time.sleep(2)

    print("Traffic simulation completed.")

traffic_control_system()
