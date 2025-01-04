mylist=[]

while True:
    print("\n Menu \n1. Create a list \n2. Update the first element \n3. Delete middle element \n4. Add n names \n5. Ccheck if python exists \n6. Exit")
    choice=input("Enter a choice")
    if choice == '1':
        mylist=input("Enter elements separated by commas :").split(',')
        mylist=[item.strip() for item in mylist]
        print("List created", mylist)

    elif choice == '2':
        mylist[0]=input("Enter new value")
        print("Updated list",mylist)

    elif choice == '3':
        mid=len(mylist)//2
        print("Deleted middle element:", mylist.pop(mid))
        print("Updated list",mid)

    elif choice == '4':
        if mylist:
            names=input("Enter name to be entered by commas:").split(',')
            mylist.extend([name.strip() for names in mylist])
            print("updated list:",mylist)
        else:
            print("Create list first")

    elif choice =='5':
        print("python is" + ("not" if 'python' not in mylist else " ") + "present in the list")
                
    elif choice =='6':
        print("Exiting")
        break

    else :
        print("Invalid option")

        
                
            
            
        
    
