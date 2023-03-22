# encode.py
# by: Adriel Barzola
# collaborators: Ernesto Lopez, Yair Temkin


def encode(user_password):
    encoded_password = ''
    for i in user_password:
        temp_element = int(i) + 3
        if temp_element >= 10:
            temp_element -= 10
        encoded_password += str(temp_element)
    print("Your password has been encoded and stored!\n")
    return encoded_password


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
            pass
        elif option == 3:
            break
