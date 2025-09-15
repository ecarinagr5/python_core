def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def convert_temperature(temperature, unit):
    if unit == 'C':
        return celsius_to_fahrenheit(temperature)  # <-- return the result
    elif unit == 'F':
        return fahrenheit_to_celsius(temperature)  # <-- return the result
    else:
        raise ValueError("Unit must be 'C' or 'F'")
