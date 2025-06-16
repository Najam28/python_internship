import os
import shutil
import random
import string


def calculator():
    print("\n--- Calculator ---")
    expr = input("Enter arithmetic expression (e.g. 2 + 3 * 4): ").strip()
    try:
        
        
        result = eval(expr, {"__builtins__": None}, {})
        print(f"Result: {result}")
    except Exception as e:
        print(f"Invalid expression: {e}")


def organize_files(source_dir, target_dir):
    if not os.path.isdir(source_dir):
        print(f"Source directory '{source_dir}' does not exist.")
        return
    os.makedirs(target_dir, exist_ok=True)
    files = [f for f in os.listdir(source_dir)
             if os.path.isfile(os.path.join(source_dir, f)) and
                (f.lower().endswith('.txt') or f.lower().endswith('.csv'))]
    if not files:
        print("No .txt or .csv files found to move.")
        return
    for f in files:
        src_path = os.path.join(source_dir, f)
        dst_path = os.path.join(target_dir, f)
        shutil.move(src_path, dst_path)
        print(f"Moved: {f}")
    print(f"Moved {len(files)} files to '{target_dir}'.")


def generate_password(length=12, use_upper=True, use_digits=True, use_special=True):
    chars = string.ascii_lowercase
    if use_upper:
        chars += string.ascii_uppercase
    if use_digits:
        chars += string.digits
    if use_special:
        chars += "!@#$%^&*()-_=+[]{}|;:,.<>?/"

    if length < 4:
        print("Password length should be at least 4.")
        return ""

    password = ''.join(random.choice(chars) for _ in range(length))
    return password
