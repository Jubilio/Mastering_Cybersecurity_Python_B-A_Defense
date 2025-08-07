# print("Hello World!")

# print("This is the main entry point of the application.")

# username = input("Please enter your username: ")
# print(f"Welcome, {username}!")


# def greet_user(username):
#     print(f"Hello, {username}! Glad to have you here.")
   
    
# greet_user(username)
# print("Thank you for using our application!")

# password = "swordfish"
# masked_password = "*" * len(password)

# print(f"Your password is: {masked_password}")

# text = "Cybersecurity"
# first_char = text[-8:]
# print(f"The first character of the text is: {first_char}")

# filename = "cmdiop.exe"

# if filename[-4:] == ".exe":
#     print("malware found")

# text = "Cybersecurity"
# print(text.upper())
# print(text.lower())
# print(text.title())
# print(text.capitalize())
# print(text.swapcase())

# password = "    swordfish    "
# print(password.strip())

# message = "User Password: passwor123"
# secure_message = message.replace("passwor123", "********")
# print(secure_message)

# email = "admin@labcyber.com"
# if email.find("@") != -1:
#     print("Valid email address")

# email = "admin@labcyber.com"
# domain = email.split("@")[-1]
# print(f"The domain of the email is: {domain}")

# url = "https://www.labcyber.com/path/to/resource"
# filename = url.split("/")[-1]
# print(f"The filename extracted from the URL is: {filename}")

email = "jubilio@labcyber.com"
username = email[:email.index("@")]
domain = email[email.index("@") + 1:]
print(f"Username: {username}, Domain: {domain}")