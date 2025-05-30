def convert_units():
    print("Mini Unit Conversion Tool")
    print("Supported conversions:")
    print("1. Meters to Feet")
    print("2. Feet to Meters")
    print("3. Inches to Centimeters")
    print("4. Centimeters to Inches")

    choice = input("Choose conversion (1-4): ").strip()

    conversions = {
        "1": ("Meters to Feet", lambda x: x * 3.28084),
        "2": ("Feet to Meters", lambda x: x / 3.28084),
        "3": ("Inches to Centimeters", lambda x: x * 2.54),
        "4": ("Centimeters to Inches", lambda x: x / 2.54),
    }

    if choice not in conversions:
        print("Invalid choice.")
        return

    desc, func = conversions[choice]
    values = input(f"Enter values to convert ({desc}), separated by commas: ").strip()

    try:
        
        nums = list(map(lambda s: float(s.strip()), values.split(',')))
        
        converted = list(map(func, nums))
        
        print(f"\nResults ({desc}):")
        for original, conv in zip(nums, converted):
            print(f"{original} -> {conv:.4f}")

    except ValueError:
        print("Please enter valid numbers separated by commas.")

if __name__ == "__main__":
    convert_units()
