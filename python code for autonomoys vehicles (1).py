import random
import time

# Possible vehicle types and their general speed ranges (in km/h)
vehicle_types = {
    "Car": (40, 120),
    "Truck": (30, 90),
    "Motorcycle": (50, 130),
    "Bus": (40, 100),
    "Bicycle": (10, 30),
    "Van": (40, 100),
}

def generate_vehicle():
    vehicle = random.choice(list(vehicle_types.keys()))
    speed_range = vehicle_types[vehicle]
    speed = random.randint(*speed_range)
    return vehicle, speed

def classify_vehicle(speed):
    if speed > 100:
        return "High-speed vehicle"
    elif 50 < speed <= 100:
        return "Medium-speed vehicle"
    else:
        return "Low-speed vehicle"

def simulate_autonomous_detection(num_vehicles=10):
    print("Autonomous Vehicle Detection System\n")
    for _ in range(num_vehicles):
        vehicle, speed = generate_vehicle()
        classification = classify_vehicle(speed)
        print(f"Detected: {vehicle} | Speed: {speed} km/h | Classification: {classification}")
        time.sleep(0.5)  # Simulate processing time

# Run the simulation
simulate_autonomous_detection()