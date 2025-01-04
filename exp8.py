while True:
    choice = input("\n Menu \n 1. Check if number is a palindrome \n 2. Check if string is a palindrome \n 3. Exit \n Enter choice: ")
    
    if choice == '1':
        num = input("Enter number: ")
        if num.isdigit() and num == num[::-1]:
            print("The number", num, "is a palindrome")
        else:
            print("The number", num, "is not a palindrome")
    
    elif choice == '2':
        s = input("Enter a string: ")
        if s == s[::-1]:  # Corrected the assignment operator to comparison
            print("The string", s, "is a palindrome")
        else:
            print("The string", s, "is not a palindrome")
    
    elif choice == '3':
        print("Exiting")
        break
    
    else:
        print("Invalid choice")
