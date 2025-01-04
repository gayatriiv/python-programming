def check_even_odd():
    try:

        number = int(input("Enter an integer: "))
        

        if number % 2 == 0:
            print(str(number) + " is even.")
        else:
            print(str(number) + " is odd.")
    
    except ValueError:
        print("Error: Please enter a valid integer.")


check_even_odd()
