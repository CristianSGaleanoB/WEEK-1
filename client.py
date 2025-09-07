import random
import requests
import json

def send_command(client_id, command_type, value):
    url = "http://localhost:5000/command"
    payload = {
        "client_id": client_id,
        "type": command_type,
        "value": value
    }
    try:
        response = requests.post(url, json=payload)
        response_data = response.json()
        if response_data["status"] == "success":
            if command_type == "speed":
                print(f"Success: Speed set to {value} units.")
            elif command_type == "toggle_switch":
                print(f"Success: Switch toggled to {'on' if value == 0 else 'off'}.")
            elif command_type == "fuel_level":
                print(f"Success: Fuel level increased by 100 units.")
        else:
            print(f"Error: {response_data['message']}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

def main_menu():
    client_id = random.randint(1, 100)
    while True:
        print("\n=== Motor Control Menu ===")
        print("1. Set Motor Speed")
        print("2. Toggle Switch")
        print("3. Increase Fuel Level")
        print("4. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            value = int(input("Enter speed value (0-100): "))
            send_command(client_id, "speed", value)
        elif choice == "2":
            send_command(client_id, "toggle_switch", 0)
        elif choice == "3":
            send_command(client_id, "fuel_level", 0)
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    print("Welcome to Motor Control Client")
    main_menu()    