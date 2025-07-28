from . import database
from . import register_graduate
from . import show_graduates
from . import show_tables




def menu():
    while True:
        print("\n📘 e-Connect Menu")
        print("1. Initialize Database")
        print("2. Register Graduate")
        print("3. Show Graduates")
        print("4. Show Tables")
        print("5. Exit")

        choice = input("Enter choice: ")
        print(f"DEBUG: User chose option {choice}")

        if choice == "1":
            print("DEBUG: Initializing DB...")
            database.init_db()
            print("DEBUG: DB Initialized")
        elif choice == "2":
            name = input("Enter name: ")
            email = input("Enter email: ")
            password = input("Enter password: ")
            print(f"DEBUG: Registering graduate {name}...")
            register_graduate.register_graduate(name, email, password)
            print(f"DEBUG: Graduate {name} registered")
        elif choice == "3":
            print("DEBUG: Showing graduates...")
            show_graduates.show_graduates()
            print("DEBUG: Graduates shown")
        elif choice == "4":
            print("DEBUG: Showing tables...")
            show_tables.show_tables()
            print("DEBUG: Tables shown")
        elif choice == "5":
            print("👋 Goodbye!")
            break
        else:
            print("❗Invalid choice. Try again.")

if __name__ == "__main__":
    menu()
