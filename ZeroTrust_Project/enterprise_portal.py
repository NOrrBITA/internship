import database_system

def start_simulation():
    print("=== Enterprise Zero Trust Simulation ===")
    user = input("Enter Employee Name: ")
    print("Select Role: 1. Administrator 2. Guest")
    choice = input("Choice (1 or 2): ")

    if choice == "1":
        print(f"\nWelcome, Admin {user}. Requesting MFA token...")
        token = "AUTH_TOKEN_99" 
        result = database_system.access_vault(token)
    else:
        print(f"\nWelcome, {user}. Guests are restricted.")
        token = "NONE"
        result = database_system.access_vault(token)

    print(f"System Response: {result}")

if __name__ == "__main__":
    start_simulation()