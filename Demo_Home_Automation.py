class HomeAutomation:
    def __init__(self):
        self.lights = {'living_room': False, 'bedroom': False, 'kitchen': False}
        self.thermostat = 70  # Initial temperature in Fahrenheit

    def toggle_light(self, room):
        if room in self.lights:
            self.lights[room] = not self.lights[room]
            print(f'{room.capitalize()} light is now {"on" if self.lights[room] else "off"}')
        else:
            print(f'No light in the {room} room.')

    def set_thermostat(self, temperature):
        if 50 <= temperature <= 90:
            self.thermostat = temperature
            print(f'Thermostat set to {self.thermostat}°F')
        else:
            print('Invalid temperature. Temperature should be between 50°F and 90°F.')

    def display_status(self):
        print("\nHome Automation Status:")
        for room, state in self.lights.items():
            print(f'{room.capitalize()} Light: {"On" if state else "Off"}')
        print(f'Thermostat Temperature: {self.thermostat}°F')


def main():
    home = HomeAutomation()

    while True:
        print("\nMenu:")
        print("1. Toggle Light")
        print("2. Set Thermostat Temperature")
        print("3. Display Status")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            room = input("Enter room (living_room, bedroom, kitchen): ")
            home.toggle_light(room)
        elif choice == '2':
            temperature = int(input("Enter thermostat temperature (50-90°F): "))
            home.set_thermostat(temperature)
        elif choice == '3':
            home.display_status()
        elif choice == '4':
            print("Exiting Home Automation System.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
