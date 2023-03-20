# menu that accepts a password, encodes it and stores it
# option to retrieve the stored encoding and the original password

def encode(user_passwd):
    encoded_passwd = ''
    for i in user_passwd:
        temp_element = int(i) + 3
        if temp_element >= 10:
            temp_element -= 10
        encoded_passwd += str(temp_element)
    print("Your password has been encoded and stored!\n")
    return encoded_passwd

def decode(encoded_password, user_passwd):
    print(f"The encoded password is {encoded_password}, and the original password is {user_passwd}.\n")


def print_menu():
    print(f"Menu\n"
          f"-------------\n"
          f"1. Encode\n"
          f"2. Decode\n"
          f"3. Quit\n")


if __name__ == "__main__":
    encoded_passwd = ''
    while True:
        print_menu()
        option = int(input("Please enter an option: "))
        if option == 1:
            user_passwd = input("Please enter your password to encode: ")
            encoded_passwd = encode(user_passwd)
        elif option == 2:
            decode(encoded_passwd, user_passwd)
        elif option == 3:
            break
