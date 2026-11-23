import string

password = input("Enter your password: ")

password_length = len(password)

has_special_characters = any(char in string.punctuation for char in password)
has_digits = any(char.isdigit() for char in password)
uppercase = any(char.isupper() for char in password)
lowercase = any(char.islower() for char in password)

most_common_passwords = ['Password', '12345678', '123456789', 'password',
                         'Aa123456', 'Pass1234', '1234567890',
                         'admin123', 'pass1111', 'abcd1234']

strength = 0
problems = 0
recommendations = []

if password == "":
    print("Password is empty")
    print("Try again")
    exit()

if password_length < 8:
    problems += 1
else:
    strength += 2

if password in most_common_passwords:
    problems += 1
else:
    strength += 1

if uppercase:
    strength += 1
else:
    problems += 1

if lowercase:
    strength += 1
else:
    problems += 1

if has_special_characters:
    strength += 1
else:
    problems += 1

if has_digits:
    strength += 1
else:
    problems += 1

print('')

if strength < 3:
    print("Strength: Weak")
elif strength < 6:
    print("Strength: Good")
elif strength >= 6:
    print("Strength: Strong")

print('')

if problems >= 1:
    print(f"Problems: {problems}")
    if password_length < 8:
        print("-Password contains less than 8 characters.")
        recommendations.append('Length matters more than complexity')
    if password in most_common_passwords:
        print("-Password is too common.")
        recommendations.append('Avoid predictable combinations')
    if uppercase:
        pass
    else:
        print("-Password does not contain an uppercase character.")
        recommendations.append('Always use upper case')
    if lowercase:
        pass
    else:
        print("-Password does not contain a lowercase character.")
        recommendations.append('Always use lower case')
    if has_special_characters:
        pass
    else:
        print("-Password does not contain special characters.")
        recommendations.append('Use special symbols to make the password stronger')
    if has_digits:
        pass
    else:
        print("-Password does not contain numbers.")
        recommendations.append('Use numbers to make the password more diverse')

print('')

if recommendations:
    print("Recommendations:")
    for recommendation in recommendations:
        print(f"- {recommendation}")
