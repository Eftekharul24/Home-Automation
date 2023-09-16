class SmartHome:
    def __init__(self):
        self.lights = {'living_room': False, 'bedroom': False, 'kitchen': False}
        self.temperature_sensor = 72  # Initial temperature in Fahrenheit

    def toggle_light(self, room):
        if room in self.lights:
            self.lights[room] = not self.lights[room]
            print(f'{room.capitalize()} light is now {"on" if self.lights[room] else "off"}')
        else:
            print(f'No light in the {room} room.')

    def read_temperature(self):
        return self.temperature_sensor

    def display_status(self):
        print("\nSmart Home Status:")
        for room, state in self.lights.items():
            print(f'{room.capitalize()} Light: {"On" if state else "Off"}')
        print(f'Temperature: {self.temperature_sensor}°F')


def main():
    smart_home = SmartHome()

    while True:
        print("\nMenu:")
        print("1. Toggle Light")
        print("2. Read Temperature")
        print("3. Display Status")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            room = input("Enter room (living_room, bedroom, kitchen): ")
            smart_home.toggle_light(room)
        elif choice == '2':
            temperature = smart_home.read_temperature()
            print(f'Current Temperature: {temperature}°F')
        elif choice == '3':
            smart_home.display_status()
        elif choice == '4':
            print("Exiting Smart Home System.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
