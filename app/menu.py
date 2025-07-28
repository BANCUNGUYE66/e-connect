from . import database
from . import register_graduate
from . import show_graduates



def menu():
    print("🟢 Menu started")
    while True:
        print("\n📘 e-Connect Menu")
        print("1. Initialize Database")
        print("2. Register Graduate")
        print("3. Show Graduates")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            database.init_db()
        elif choice == "2":
            name = input("Enter name: ")
            email = input("Enter email: ")
            password = input("Enter password: ")
            register_graduate.register_graduate(name, email, password)
        elif choice == "3":
            show_graduates.show_graduates()
        elif choice == "4":
            print("👋 Goodbye!")
            break
        else:
            print("❗Invalid choice. Try again.")

if __name__ == "__main__":
    menu()
