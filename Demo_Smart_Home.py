import time

class Light:
    def __init__(self):
        self.state = False

    def turn_on(self):
        self.state = True
        print("Light is ON")

    def turn_off(self):
        self.state = False
        print("Light is OFF")

    def status(self):
        return "ON" if self.state else "OFF"

class Thermostat:
    def __init__(self):
        self.temperature = 72

    def set_temperature(self, temperature):
        self.temperature = temperature
        print(f"Thermostat set to {temperature}°F")

    def get_temperature(self):
        return self.temperature

def main():
    living_room_light = Light()
    kitchen_light = Light()
    thermostat = Thermostat()

    while True:
        print("\nSmart Home System Menu:")
        print("1. Turn Living Room Light On")
        print("2. Turn Living Room Light Off")
        print("3. Turn Kitchen Light On")
        print("4. Turn Kitchen Light Off")
        print("5. Set Thermostat Temperature")
        print("6. Check Thermostat Temperature")
        print("7. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            living_room_light.turn_on()
        elif choice == '2':
            living_room_light.turn_off()
        elif choice == '3':
            kitchen_light.turn_on()
        elif choice == '4':
            kitchen_light.turn_off()
        elif choice == '5':
            temperature = int(input("Enter thermostat temperature (in °F): "))
            thermostat.set_temperature(temperature)
        elif choice == '6':
            current_temperature = thermostat.get_temperature()
            print(f"Current thermostat temperature: {current_temperature}°F")
        elif choice == '7':
            print("Exiting Smart Home System.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
