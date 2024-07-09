passwords = []

password = input()

while password != 'exit':
    if len(password) >= 8 and not(password.isalpha()) and not(password.lower() == password):
        passwords.append(password)
    else:
        print('incorrect password')
    password = input()


print(passwords)