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

def decode(encoded_passwd):
    # Check if encoded password is exactly 8 digits long
    if len(encoded_passwd) != 8:
        raise ValueError("Encoded password must be exactly 8 digits long")
    # Decode each digit by shifting it down by 3
    decoded_digits = []
    for digit in encoded_passwd:
        # Convert digit from string to integer
        digit_int = int(digit)
        # Shift digit down by 3, wrapping around to 9 after 0
        decoded_digit_int = (digit_int - 3) % 10
        # Convert decoded digit back to string and append to list
        decoded_digits.append(str(decoded_digit_int))
    # Convert list of decoded digits to string
    decoded_password = ''.join(decoded_digits)
    return decoded_password

if __name__ == "__main__":
    encoded_passwd = ''
    while True:
        print_menu()
        option = int(input("Please enter an option: "))
        if option == 1:
            user_passwd = input("Please enter your password to encode: ")
            encoded_passwd = encode(user_passwd)
        elif option == 2:
            decoded_passwd = decode(encoded_passwd)
            # Print the original and encoded password
            print(f"The encoded password is {encoded_passwd}, and the original password is {decoded_passwd}.")
        elif option == 3:
            break

# this is a comment
