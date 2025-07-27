from app.auth import register_graduate, login_graduate

def main_menu():
    while True:
        print("\n========== e-Connect ==========")
        print("1. Graduate Login")
        print("2. Graduate Register")
        print("3. Company Login")
        print("4. Company Register")
        print("5. Admin Access (Coming Soon)")
        print("0. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            login_graduate()
        elif choice == '2':
            register_graduate()
        elif choice == '3':
            print("Company Login - Not implemented yet.")
        elif choice == '4':
            print("Company Register - Not implemented yet.")
        elif choice == '5':
            print("Admin access is under development.")
        elif choice == '0':
            print("Thanks for using e-Connect!")
            break
        else:
            print("Invalid choice. Please try again.")