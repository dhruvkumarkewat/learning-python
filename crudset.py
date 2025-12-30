my_set = set()

while True:
    print("\n--- MENU ---")
    print("Press 1 for Create")
    print("Press 2 for Read")
    print("Press 3 for Update")
    print("Press 4 for Delete")
    print("Press 5 for Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        print("CREATE DATA IN SET")
        n = int(input("Enter the no of data: "))
        for i in range(n):
            data = input(f"Enter the {i+1} data: ")
            my_set.add(data)   # add instead of append
        print("Data inserted successfully.")

    elif ch == 2:
        print("READ DATA FROM SET")
        while True:
            print("\n1. Show all data")
            print("2. Search specific data")
            print("3. Exit reading")
            sub_ch = int(input("Enter your choice: "))

            if sub_ch == 1:
                print("All data:", my_set)
            elif sub_ch == 2:
                n = input("Enter the data to search: ")
                if n in my_set:
                    print(f"'{n}' found in set")
                else:
                    print("Data not found")
            elif sub_ch == 3:
                print("Exiting read mode.")
                break
            else:
                print("Invalid choice, try again.")

    elif ch == 3:
        print("UPDATE DATA IN SET")
        old_data = input("Enter the data to update: ")
        if old_data in my_set:
            new_data = input("Enter the new data: ")
            my_set.remove(old_data)
            my_set.add(new_data)
            print("Data updated successfully.")
        else:
            print("Data not found in set.")

    elif ch == 4:
        print("DELETE DATA FROM SET")
        data = input("Enter the data to delete: ")
        if data in my_set:
            my_set.remove(data)
            print("Data deleted successfully.")
        else:
            print("Data not found in set.")

    elif ch == 5:
        print("EXITING PROGRAM")
        break

    else:
        print("Wrong choice! Please try again.")