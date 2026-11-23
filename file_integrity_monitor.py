import hashlib

import sys

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
