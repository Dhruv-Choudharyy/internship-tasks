def celsius_to_fahrenheit(celsius):
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit

def celsius_to_kelvin(celsius):
    kelvin = celsius + 273.15
    return kelvin

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def fahrenheit_to_kelvin(fahrenheit):
    kelvin = (fahrenheit + 459.67) * 5/9
    return kelvin

def kelvin_to_celsius(kelvin):
    celsius = kelvin - 273.15
    return celsius

def kelvin_to_fahrenheit(kelvin):
    fahrenheit = kelvin * 9/5 - 459.67
    return fahrenheit

def main():
    print("Temperature Conversion Program")
    print("-------------------------------")
    print("Select the original unit of measurement:")
    print("1. Celsius")
    print("2. Fahrenheit")
    print("3. Kelvin")
    
    choice = input("Enter your choice (1/2/3): ")
    
    if choice == '1':
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        kelvin = celsius_to_kelvin(celsius)
        print(f"{celsius} degrees Celsius is equal to:")
        print(f"{fahrenheit} degrees Fahrenheit")
        print(f"{kelvin} Kelvin")
        
    elif choice == '2':
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = fahrenheit_to_celsius(fahrenheit)
        kelvin = fahrenheit_to_kelvin(fahrenheit)
        print(f"{fahrenheit} degrees Fahrenheit is equal to:")
        print(f"{celsius} degrees Celsius")
        print(f"{kelvin} Kelvin")
        
    elif choice == '3':
        kelvin = float(input("Enter temperature in Kelvin: "))
        celsius = kelvin_to_celsius(kelvin)
        fahrenheit = kelvin_to_fahrenheit(kelvin)
        print(f"{kelvin} Kelvin is equal to:")
        print(f"{celsius} degrees Celsius")
        print(f"{fahrenheit} degrees Fahrenheit")
        
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()