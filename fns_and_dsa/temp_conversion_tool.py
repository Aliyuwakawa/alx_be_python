# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    """Converts a temperature from Fahrenheit to Celsius."""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """Converts a temperature from Celsius to Fahrenheit."""
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32

def main():
    try:
        # Prompt user for temperature and unit
        temperature = float(input("Enter the temperature: "))
        unit = input("Specify the unit (Celsius or Fahrenheit): ").strip().lower()

        # Determine the conversion based on the unit
        if unit in ['c', 'celsius']:
            converted_temperature = convert_to_fahrenheit(temperature)
            print(f"{temperature}° Celsius is {converted_temperature:.2f}° Fahrenheit")
        elif unit in ['f', 'fahrenheit']:
            converted_temperature = convert_to_celsius(temperature)
            print(f"{temperature}° Fahrenheit is {converted_temperature:.2f}° Celsius")
        else:
            raise ValueError("Invalid unit. Please specify 'Celsius' or 'Fahrenheit'.")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()

