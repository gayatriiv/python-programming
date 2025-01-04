d1={}
d2={}

def dict1():
    global d1
    n=int(input("Enter number of values:"))
    for i in range (0,n):
        key=int(input("Enter key(int):"))
        value=input("Enter value:")
        d1.update({key:value})
    print("The dictionary is: ",d1)
    
def dict2():
    global d2
    n=int(input("Enter number of values:"))
    for i in range (0,n):
        key=int(input("Enter key(int):"))
        value=input("Enter value:")
        d2.update({key:value})
    print("The dictionary is: ",d2)

def dict_update():
    print("Dictionary:",d2,"will be concatenated to:",d1)
    d1.update(d2)
    print("Dictionary after concatenation:",d1)

    k =int(input("\nEnter key of value to be updated:"))
    val = input("Enter value to be updated:")
    if k in d1:
        d1[k]=val
        print("Updated dictionary is ",d1)

def dict_delete():
    m=int(input("Enter key of value to be deleted:"))
    if m in d1:
        print("Value to be deleted:",d1[m])
        del d1[m]
        print("Dictionary after deletion:",d1)
    else:
        print("Key not present in Dictionary")

def dict_find():
    m=int(input("Enter key to be searched:"))
    if m in d1:
        print("The key value is:",d1[m])
    else:
        print("Key not present in Dictionary")

def dict_map():
    key=[] 
    values=[]
    n=int(input("Enter no of elements:"))
    for i in range (0,n):
        ekey=int(input("Enter key:"))
        key.append(ekey)
        evalue=input("Enter value:")
        values.append(evalue)
    print("Key list:",key,"\nValue list:",values)
    Dict3=dict(zip(key,values))
    print("Dictionary after mapping:",Dict3)    
    

choice=0
while(choice!=6):
    print("-------------------------------------------------")
    print('1.Enter first Dictionary\n2.Enter second Dictionary\n3.Update Dictionary and Delete an element\n4.Find a key and print its value\n5.Map two list into dictionary\n6.Exit')
    choice=int(input('Enter Choice:'))
    if choice==1:
        dict1()
    elif choice==2:
        dict2()   
    elif choice==3:
        dict_update()
        dict_delete()
    elif choice==4:
        dict_find()
    elif choice==5:
        dict_map()
    else:
        exit(0)
