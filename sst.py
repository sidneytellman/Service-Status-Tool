from service import services
from functions import show_all, show_one, add_service, change_status, remove_service, show_menu


def main():
    print("=== Service Status Tool ===")

    while True:
        show_menu()
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            show_all(services)
        elif choice == "2":
            show_one(services)
        elif choice == "3":
            add_service(services)
        elif choice == "4":
            change_status(services)
        elif choice == "5":
            remove_service(services)
        elif choice == "6":
            print("Exiting the service status tool.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()