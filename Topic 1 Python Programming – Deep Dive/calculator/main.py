from calculator import calculator, organize_files, generate_password

def main():
    print("=== Modular CLI Toolkit ===")

    while True:
        print("\nSelect a tool:")
        print("1. Calculator")
        print("2. File Organizer")
        print("3. Password Generator")
        print("4. Exit")

        choice = input("Enter choice (1-4): ").strip()

        if choice == "1":
            calculator()

        elif choice == "2":
            src = input("Enter source directory: ").strip()
            dst = input("Enter target directory: ").strip()
            organize_files(src, dst)

        elif choice == "3":
            try:
                length = int(input("Enter password length (default 12): ").strip() or 12)
            except ValueError:
                print("Invalid number, using default length 12.")
                length = 12
            use_upper = input("Use uppercase letters? (y/n, default y): ").strip().lower() != 'n'
            use_digits = input("Use digits? (y/n, default y): ").strip().lower() != 'n'
            use_special = input("Use special characters? (y/n, default y): ").strip().lower() != 'n'

            pwd = generate_password(length, use_upper, use_digits, use_special)
            if pwd:
                print(f"Generated password: {pwd}")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice, please enter 1-4.")

if __name__ == "__main__":
    main()
