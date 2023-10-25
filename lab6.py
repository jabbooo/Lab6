
def main():
    user_password = input('What do you want to encode?')
    encoder(user_password)

def encoder(user_password):
    for num in user_password:
        encoded_password = num + 3
        print(encoded_password)



if __name__ == '__main__':
   main()