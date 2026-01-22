#7. Write a program to create a list and perform various operations on list using menu.#

def display():
    print("\n--- List operations Menu ---")
    print("1. Create list")
    print("2. Add element")
    print("3. Remove element")
    print("4. Display list")
    print("5. Sort list")
    print("6. Find length of list")
    print("7. Exit")

my_list = []

while True:
    display()
    choice = int(input("Enter your choice: "))

    if choice == 1:
        my_list = list(map(int, input("Enter elements separated by space: ").split()))
        print("List created successfully.")

    elif choice == 2:
        element = int(input("Enter element to add: "))
        my_list.append(element)
        print("Element added.")

    elif choice == 3:
        element = int(input("Enter element to remove: "))
        if element in my_list:
            my_list.remove(element)
            print("Element removed.")
        else:
            print("Element not found in list.")

    elif choice == 4:
        print("Current List:", my_list)

    elif choice == 5:
        my_list.sort()
        print("List sorted:", my_list)

    elif choice == 6:
        print("Length of list:", len(my_list))

    elif choice == 7:
        print("Exiting program.")
        break

    else:
        print("Invalid choice. Please try again.")
