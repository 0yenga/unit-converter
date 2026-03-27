
```markdown
# Unit Converter

A command-line unit conversion program written in Python.  
Supports conversions for length, temperature, and mass.

## Features

### Length
- Kilometers to Miles
- Miles to Kilometers

### Temperature
- Celsius to Fahrenheit
- Fahrenheit to Celsius

### Mass
- Kilograms to Pounds
- Pounds to Kilograms

## Requirements

- Python 3.x
- No external libraries required

## Installation

1. Verify Python is installed:
```bash
python --version
```

2. Clone the repository:
```bash
git clone https://github.com/0yenga/unit-converter.git
cd unit-converter
```

3. Run the program:
```bash
python converter.py
```

## Usage

The program presents a main menu with four options:

```
==================================================
                  UNIT CONVERTER
==================================================
1. Length conversions
2. Temperature conversions
3. Mass conversions
4. Quit
```

Select a category, choose a conversion type, enter your value, and the result 
will be displayed.

Example:
```
--- Conversion: Celsius -> Fahrenheit ---
Enter temperature in Celsius: 25
25.0C = 77.0F
```

## Code Structure

- **Display functions** — `display_*_menu()` : Handle menu rendering
- **Conversion functions** — `*_to_*()` : Implement conversion formulas
- **Handler functions** — `handle_*_conversions()` : Manage interactive logic
- **Utility function** — `get_valid_number()` : Validate numeric input
- **Main function** — `main()` : Program entry point and flow control

## Conversion Formulas

| Conversion | Formula |
|---|---|
| km → miles | miles = km × 0.621371 |
| miles → km | km = miles / 0.621371 |
| °C → °F | F = (C × 9/5) + 32 |
| °F → °C | C = (F - 32) × 5/9 |
| kg → pounds | pounds = kg × 2.20462 |
| pounds → kg | kg = pounds / 2.20462 |

## Error Handling

- Non-numeric values are rejected with an error message
- Invalid menu selections prompt the user to try again

## Author

ADJAMBO Espoir Oyénga — Computer Engineering Student  
Nizhny Novgorod State Technical University, Russia  
[GitHub Profile](https://github.com/0yenga)
```
