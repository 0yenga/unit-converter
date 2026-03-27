#!/usr/bin/env python3
"""
Unit Converter - Command line program for converting between different units
Supports: length, temperature, mass
"""

def display_main_menu():
    """Display the main program menu"""
    print("\n" + "="*50)
    print("UNIT CONVERTER".center(50))
    print("="*50)
    print("1. Length conversions")
    print("2. Temperature conversions")
    print("3. Mass conversions")
    print("4. Quit")
    print("-"*50)

def display_length_menu():
    """Display the length conversion menu"""
    print("\n" + "-"*40)
    print("LENGTH CONVERSIONS".center(40))
    print("-"*40)
    print("1. Kilometers -> Miles")
    print("2. Miles -> Kilometers")
    print("3. Return to main menu")
    print("-"*40)

def display_temperature_menu():
    """Display the temperature conversion menu"""
    print("\n" + "-"*40)
    print("TEMPERATURE CONVERSIONS".center(40))
    print("-"*40)
    print("1. Celsius -> Fahrenheit")
    print("2. Fahrenheit -> Celsius")
    print("3. Return to main menu")
    print("-"*40)

def display_mass_menu():
    """Display the mass conversion menu"""
    print("\n" + "-"*40)
    print("MASS CONVERSIONS".center(40))
    print("-"*40)
    print("1. Kilograms -> Pounds")
    print("2. Pounds -> Kilograms")
    print("3. Return to main menu")
    print("-"*40)

def km_to_miles(km):
    """Convert kilometers to miles"""
    return km * 0.621371

def miles_to_km(miles):
    """Convert miles to kilometers"""
    return miles / 0.621371

def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit"""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius"""
    return (fahrenheit - 32) * 5/9

def kg_to_pounds(kg):
    """Convert kilograms to pounds"""
    return kg * 2.20462

def pounds_to_kg(pounds):
    """Convert pounds to kilograms"""
    return pounds / 2.20462

def get_valid_number(prompt):
    """
    Prompt user for a valid number
    Continues until a valid number is entered
    """
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Error: Please enter a valid number (e.g., 10, 25.5)")

def handle_length_conversions():
    """Handle length conversion operations"""
    while True:
        display_length_menu()
        choice = input("\nYour choice (1-3): ")
        
        if choice == '1':
            print("\n--- Conversion: Kilometers -> Miles ---")
            km = get_valid_number("Enter distance in kilometers: ")
            miles = km_to_miles(km)
            print(f"\n{km} kilometer(s) = {miles:.2f} mile(s)")
            input("\nPress Enter to continue...")
            
        elif choice == '2':
            print("\n--- Conversion: Miles -> Kilometers ---")
            miles = get_valid_number("Enter distance in miles: ")
            km = miles_to_km(miles)
            print(f"\n{miles} mile(s) = {km:.2f} kilometer(s)")
            input("\nPress Enter to continue...")
            
        elif choice == '3':
            break
            
        else:
            print("\nInvalid choice. Please select 1, 2, or 3.")
            input("Press Enter to continue...")

def handle_temperature_conversions():
    """Handle temperature conversion operations"""
    while True:
        display_temperature_menu()
        choice = input("\nYour choice (1-3): ")
        
        if choice == '1':
            print("\n--- Conversion: Celsius -> Fahrenheit ---")
            celsius = get_valid_number("Enter temperature in Celsius: ")
            fahrenheit = celsius_to_fahrenheit(celsius)
            print(f"\n{celsius}C = {fahrenheit:.1f}F")
            input("\nPress Enter to continue...")
            
        elif choice == '2':
            print("\n--- Conversion: Fahrenheit -> Celsius ---")
            fahrenheit = get_valid_number("Enter temperature in Fahrenheit: ")
            celsius = fahrenheit_to_celsius(fahrenheit)
            print(f"\n{fahrenheit}F = {celsius:.1f}C")
            input("\nPress Enter to continue...")
            
        elif choice == '3':
            break
            
        else:
            print("\nInvalid choice. Please select 1, 2, or 3.")
            input("Press Enter to continue...")

def handle_mass_conversions():
    """Handle mass conversion operations"""
    while True:
        display_mass_menu()
        choice = input("\nYour choice (1-3): ")
        
        if choice == '1':
            print("\n--- Conversion: Kilograms -> Pounds ---")
            kg = get_valid_number("Enter mass in kilograms: ")
            pounds = kg_to_pounds(kg)
            print(f"\n{kg} kilogram(s) = {pounds:.2f} pound(s)")
            input("\nPress Enter to continue...")
            
        elif choice == '2':
            print("\n--- Conversion: Pounds -> Kilograms ---")
            pounds = get_valid_number("Enter mass in pounds: ")
            kg = pounds_to_kg(pounds)
            print(f"\n{pounds} pound(s) = {kg:.2f} kilogram(s)")
            input("\nPress Enter to continue...")
            
        elif choice == '3':
            break
            
        else:
            print("\nInvalid choice. Please select 1, 2, or 3.")
            input("Press Enter to continue...")

def main():
    """Main program function"""
    print("\n" + "="*60)
    print("WELCOME TO THE UNIT CONVERTER".center(60, "="))
    print("="*60)
    
    while True:
        display_main_menu()
        choice = input("\nYour choice (1-4): ")
        
        if choice == '1':
            handle_length_conversions()
        elif choice == '2':
            handle_temperature_conversions()
        elif choice == '3':
            handle_mass_conversions()
        elif choice == '4':
            print("\n" + "="*50)
            print("Thank you for using the unit converter.".center(50, "="))
            print("="*50 + "\n")
            break
        else:
            print("\nInvalid choice. Please select 1, 2, 3, or 4.")
            input("Press Enter to continue...")

if __name__ == "__main__":
    main()
