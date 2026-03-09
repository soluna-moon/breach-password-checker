common_passwords = ["123456", "password", "qwerty", "111111", "admin", "letmein"]

password = input("Enter a password to check: ")

if password in common_passwords:
    print("Warning: This password is very common and insecure!")
else:
    print("This password seems safer.")