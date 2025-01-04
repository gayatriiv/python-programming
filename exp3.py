even = []
odd = []
merged = []

def enter_numbers():
    nums = input("Enter numbers separated by commas: ")
    for num in nums.split(','):
        num = int(num.strip())
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)

def merge_and_sort():
    global merged
    merged = even + odd
    merged.sort()
    print("Merged and sorted list:", merged)

def find_max_min():
    if merged:
        print('Maximum:', max(merged))
        print('Minimum:', min(merged))
    else:
        print("Merged list is empty.")

def display_lists():
    print("Even list:", even)
    print("Odd list:", odd)

def menu():
    print("\nMenu:")
    print("1. Enter numbers")
    print("2. Show even and odd lists")
    print("3. Merge and sort lists")
    print("4. Find max and min from the merged list")
    print("5. Exit")

def main():
    while True:
        menu()
        choice = int(input("Enter choice: "))
        
        if choice == 1:
            enter_numbers()
        elif choice == 2:
            display_lists()
        elif choice == 3:
            merge_and_sort()
        elif choice == 4:
            find_max_min()
        elif choice == 5:
            print("Exiting.")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
main()
