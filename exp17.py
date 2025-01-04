import os

def getChoice():
    print("\n------------------------------------------------")
    print("Menu\n","(A) append data to existing file and then display the entire file \n",
"(B) count the number of lines, words and characters in a file. \n",
"(C) display file available in current directory \n","(Q)uit")
    choose=input("Enter your choice: ")
    choice=choose.lower()

    return choice


def fileFirstFunc():

    fileName1 = input("Enter file to read the content from: ")#Test.txt
    fileName2 = input("Enter file to append content: ")#Sample.txt
    f1 = open(fileName1, "r")#Test.txt is opened in read mode
    data2 = f1.read()
    f1.close()
    f2 = open(fileName2, "a")#Sample.txt is opened in append mode
    f2.write("\n")
    f2.write(data2)
    f2.close()
    f2 = open(fileName2, "r")
    line=f2.readline()
    print("Contents of the new file after appending data")
    while(line!=""):
        print(line,end="")
        line=f2.readline()
    f2.close()
    

def fileSecondFunc():
    
    num_lines = 0
    num_words = 0
    num_char = 0
    f = open("Test.txt", "r")
    for line in f:
        num_lines = num_lines + 1
        words = line.split()
        print("Words after spliting in line",num_lines,": ",words)
        num_words = num_words + len(words)
    # Again set the pointer to the beginning
    f.seek(0,0)
    data = f.read()
    num_char = len(data)
    print("Number of lines:")
    print(num_lines)
    print("Number of words:")
    print(num_words)
    print("Number of Character including white spaces")
    print(num_char)

def fileThirdFunc():
    cwd = os.getcwd()
    print("Current working directory:", cwd)
    for root, dirs, files in os.walk("."):
        print(root,dirs)
        for filename in files:
            print(filename)
            

choice = getChoice()
while choice!="q":
    if choice == "a":
        fileFirstFunc() 
    elif choice=="b":
        fileSecondFunc()
    elif choice=="c":
        fileThirdFunc()
    else:
        print("Invalid choice, please choose again")
        print("\n")

    choice = getChoice()
