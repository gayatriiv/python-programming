mylist = []

while True:
    print("\nMenu:\n1. Create list\n2. Update first element\n3. Delete middle element\n4. Add names\n5. Check for 'python'\n6. Exit")
    choice = input("Choose an option: ")

    if choice == '1':
        mylist = input("Enter elements separated by commas: ").split(',')
        mylist = [item.strip() for item in mylist]
        print("List created:", mylist)
    
    elif choice == '2':
        mylist[0] = input("Enter new value for the first element: ")
        print("Updated list:", mylist)
    
    elif choice == '3':
        mid = len(mylist) // 2
        print("Deleted middle element:", mylist.pop(mid))
        print("Updated list:", mylist)
    
    elif choice == '4':
        if mylist:
            names = input("Enter names separated by commas: ").split(',')
            mylist.extend([name.strip() for name in names])
            print("Updated list:", mylist)
        else:
            print("Create a list first.")
    
    elif choice == '5':
        print("'python' is" + (" not " if 'python' not in mylist else " ") + "present in the list.")
    
    elif choice == '6':
        print("Exiting.")
        break
    
    else:
        print("Invalid choice or empty list.")
