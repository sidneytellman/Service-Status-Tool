def show_all(services):
    print()

    for service in services:
        print(f"{service['name']:<15} {service['status']:<10} {service['Response_Time']} ms")

    print()


def show_one(services):
    service_name = input("Enter the name of the service to check: ").strip()

    for service in services:
        if service["name"] == service_name:
            print(f"{service_name} - {service['status']}")
            return

    print("Service cannot be found.")


def add_service(services):
    service_name = input("New service: ").strip()

    new_service = {
        "name": service_name,
        "status": "unknown",
        "Response_Time": 0
    }

    services.append(new_service)
    print(f"{service_name} added.")


def change_status(services):
    service_name = input("Service to change: ").strip()

    for service in services:
        if service["name"] == service_name:
            service["status"] = input("New status: ").strip()
            print(f"{service_name} is now {service['status']}.")
            return

    print("Service not found.")


def remove_service(services):
    service_name = input("Enter the name of the service to remove: ").strip()

    for service in services:
        if service["name"] == service_name:
            services.remove(service)
            print()
            print(f"Service '{service_name}' removed.")
            print()
            return

    print()
    print(f"Service '{service_name}' not found.")


def show_menu():
    print()
    print("1. List services")
    print("2. Check service status")
    print("3. Add service")
    print("4. Change status")
    print("5. Remove service")
    print("6. Exit")