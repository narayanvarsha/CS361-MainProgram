import json
import time

def load_accounts():
    try:
        with open('accounts.json', 'r') as file:
            accounts = json.load(file)
    except FileNotFoundError:
        accounts = {}
    return accounts

def save_accounts(accounts):
    with open('accounts.json', 'w') as file:
        json.dump(accounts, file)

def create_account():
    accounts = load_accounts()
    username = input("Enter username: ")
    if username in accounts:
        print("This account username already exists.")
        return
    print("Note: Ensure your password is strong.")
    password = input("Enter password: ")
    start_time = time.time()
    accounts[username] = password
    save_accounts(accounts)
    end_time = time.time()
    print(f"Account created in {end_time:.2f} seconds.")
    print("Benefit: You can now log in with this account.")

def update_account():
    accounts = load_accounts()
    username = input("Enter username: ")
    if username not in accounts:
        print("Account does not exist!")
        return
    print("Note: Choose a strong password to enhance security.")
    new_password = input("Enter new password: ")
    start_time = time.time()
    accounts[username] = new_password
    save_accounts(accounts)
    end_time = time.time()
    print(f"Account updated in {end_time:.2f} seconds.")
    print("Benefit: Your account password has been updated.")

def delete_account():
    accounts = load_accounts()
    username = input("Enter username: ")
    if username not in accounts:
        print("Account does not exist!")
        return
    print("Note: Deleting an account will permanently remove it and cannot be undone.")
    confirmation = input("Are you sure you want to delete this account? (yes/no): ")
    if confirmation.lower() != 'yes':
        print("Account deletion cancelled.")
        return
    start_time = time.time()
    del accounts[username]
    save_accounts(accounts)
    end_time = time.time()
    print(f"Account deleted in {end_time:.2f} seconds.")

def view_accounts():
    accounts = load_accounts()
    if not accounts:
        print("No accounts found.")
        return
    print("Current accounts:")
    for user in accounts:
        print(f"- {user}")

def main():
    print("\n Welcome to the Account Management System!")
    print("\n This system allows you to manage user accounts.")
    
    while True:
        print("\n1. Create account: Register a new user.\n2. Update account: Change your existing password.\n3. Delete account: Delete your user account.\n4. View accounts: List all current accounts.\n5. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            create_account()
        elif choice == '2':
            update_account()
        elif choice == '3':
            delete_account()
        elif choice == '4':
            view_accounts()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
