from is_palindromae import is_palindrome



if __name__ == '__main__':
    while True:
        try:
            x = int(input("Enter an integer:  "))

            if is_palindrome(x):
                print(f"{x} is a palindrome.")
            else:
                print(f"{x} is not a palindrome.")
        except ValueError:
            print("You must enter an integer!")
            break
