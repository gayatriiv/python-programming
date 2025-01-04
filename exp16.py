class IncorrectPasswordError(Exception):
    pass

correct_password = "55"
attempts = 3
count = 0

while count < attempts:
    count += 1
    try:
        print("Attempt {}/{}".format(count, attempts))
        entered_password = input("Enter your password: ")
        if entered_password != correct_password:
            raise IncorrectPasswordError

        print("Access Granted!")
        print("You guessed the password in",count,"attempt(s).")
        break

    except IncorrectPasswordError:
        print("Incorrect password, please try again!")

    if count == attempts:
        print("Sorry, you've used all 3 attempts. Access Denied.")
