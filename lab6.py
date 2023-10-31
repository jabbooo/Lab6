
# Hayden Stone

def main():
    while True:
        menu()
        menu_choice = int(input('Please enter an option: '))
        if menu_choice == 1:
            user_password = input('Please enter your password to encode: ')
            encoded_password = encoder(user_password)
            print('Your password has been encoded and stored!')
        elif menu_choice == 2:
            decoder(encoded_password)
            print(f'The encoded password is {encoded_password}, and the original password is {user_password}.')
        elif menu_choice == 3:
            exit()


def menu():
    print('''
Menu
-------------
1. Encode
2. Decode
3. Quit
''')

def encoder(user_password):
    encoded_password = ''
    num = 0
    for num in user_password:
        num = int(num)
        num += 3
        if num > 9:
            num = num % 9
        encoded_password += str(num)  
    return encoded_password
    
def decoder(encoded_password):
    user_password = ''
    for i in encoded_password:
        i = int(i)
        i -= 3
        user_password += str(i)
    return user_password


if __name__ == '__main__':
   main()