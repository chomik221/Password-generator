
# import password manager package
from password_manager_package import generate_password, add_password, remove_password, change_password, list_passwords

# print result

def print_result(result_message, result):
    print(f"{result_message} {result}")

# choose operation 

def choose_operation():
    while True:
        choose_option = input("Add password: 'A',  Remove password: 'R', Change password: 'C', List passwords: 'L': ").lower()
        if choose_option == 'a':
            return 'add'
        elif choose_option == 'r':
            return 'remove'
        elif choose_option == 'c':
            return 'change'
        elif choose_option == 'l':
            return 'list'
        else:
            print("Invalid option. Please try again.")


# choose service
def choose_service():
    while True:
        choose_option = input("Choose service: Email: 'E', Facebook: 'F', Twitter: 'T', Instagram: 'I': ").lower()
        services = {'e': 'Email', 'f': 'Facebook', 't': 'Twitter', 'i': 'Instagram'}
        if choose_option in services:
            return services[choose_option]
        else:
            print("Invalid service. Please try again.")

# add password

def add_new_password():
    service = choose_service()
    username = input("Enter your user name: ")
    password = generate_password()
    add_password(service, username, password)

# remove password

def delete_password():
    service = choose_service()
    username = input('Please enter your username: ')
    remove_password(service, username)

# change password 

def password_update():
    service = choose_service()
    username = input("Please enter your username: ")
    new_password = generate_password()
    change_password(service, username, new_password)

# run program 

def run_program(choosen_operation):
    if choosen_operation == 'add':
        add_new_password()
    elif choosen_operation == 'remove':
        delete_password()
    elif choosen_operation == 'change':
        password_update()
    elif choosen_operation == 'list':
        list_passwords()

choosen_operation = choose_operation()

while True:
    choosen_operation = choose_operation()
    run_program(choosen_operation)
    again = input("Do you want to perform another action? (Y/N): ").lower()
    if again != 'y':
        print("Exiting program.")
        break

