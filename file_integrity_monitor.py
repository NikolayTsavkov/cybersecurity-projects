import hashlib
import sys

# Hash Calculator

def calculate_hash():
    try:
        input_file = input("Enter file path: ")
        with open(input_file, "rb") as f:
            data = f.read()

        hashed_file = hashlib.sha256(data).hexdigest()

        output_file = input("Enter output file path: ")

        if output_file == input_file:
            print("The output file is the same as the input file.")
            print("Do you wish to overwrite the input file? (Yes/No)")

            while True:
                answer = input("Yes/No: ").strip().lower()

                if answer == "yes":
                    break
                elif answer == "no":
                    sys.exit(0)
                else:
                    print("Please enter Yes/No.")
                    continue

        with open(output_file, "w") as f:
            f.write(hashed_file)

    except FileNotFoundError:
        print("File not found.")
    except PermissionError:
        print("Permission denied.")
    except IsADirectoryError:
        print("The specified path is a directory.")
    except OSError:
        print("OS error occurred.")
    else:
        print(f"File: {input_file}")
        print(f"SHA-256: {hashed_file}")
        print(f"Hashed file: {output_file}")

# File Integrity Checker

def verify_integrity():
    original_file = input("Enter original file path: ")
    stored_hash_file = input("Enter hashed file path: ")

    try:
        with open(original_file, "rb") as f:
            original_data = f.read()

        calculated_hash = hashlib.sha256(original_data).hexdigest()

        with open(stored_hash_file, "r") as f:
            stored_hash = f.read().strip()

    except FileNotFoundError:
        print("File not found.")
    except PermissionError:
        print("Permission denied.")
    except IsADirectoryError:
        print("The specified path is a directory.")
    except OSError:
        print("OS error occurred.")
    else:
        if calculated_hash == stored_hash:
            print("[OK] File integrity verified.")
            print("No modifications detected.")
        else:
            print("[WARNING] File integrity compromised!")
            print("The calculated hash does not match the stored hash!")

# Main menu

def main():
    while True:
        print("1. Calculate and save file hash")
        print("2. Verify file integrity")
        print("3. Exit")
        menu_choice = input("Enter your choice: ")
        if menu_choice == '1':
            calculate_hash()
        elif menu_choice == '2':
            verify_integrity()
        elif menu_choice == '3':
            print("Thank you for using this tool!")
            sys.exit(0)
        else:
            print("Please enter number between 1 and 3.")

main()

