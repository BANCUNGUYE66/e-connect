from app.database import init_db
from app.menu import main_menu

def main():
    init_db()
    print("Welcome to e-Connect!")
    main_menu()

if __name__ == "__main__":
    main()