while True:
    print("1. CELSIUS TO FAHRENHEIT")
    print("2. FAHRENHEIT TO CELSIUS")
    print("3. EXIT")
    
    choice = input("ENTER YOUR CHOICE: ")
    
    # Ensure the input is an integer
    try:
        ch = int(choice)
    except ValueError:
        print("Please enter a valid number.")
        continue
    
    if ch == 1:
        c = float(input("ENTER TEMPERATURE IN CELSIUS: "))
        f = ((9 * c) / 5) + 32
        print("Converted temperature is:", f)
    
    elif ch == 2:
        f = float(input("ENTER TEMPERATURE IN FAHRENHEIT: "))
        c = ((f - 32) / 9) * 5
        print("Converted temperature is:", c)
    
    elif ch == 3:
        print("Exiting the program.")
        break  
    
    else:
        print("Wrong choice. Please try again.")
