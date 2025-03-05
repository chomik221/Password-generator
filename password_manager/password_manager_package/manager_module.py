# manager module

# pasword dictionary 

password_dictionary = {
    'Email': [],
    'Facebook': [],
    'Twitter': [],
    'Instagram': []
}

# add password

def add_password(service, username, password):
    if service in password_dictionary:
        password_dictionary[service].append((username, password))
        print(f"Account {username} was added to {service}")
    else:
        print("Service doesn't exist")

# remove password

def remove_password(service, username):
    if service in password_dictionary:
        user_found = False
        for i, (user, _) in enumerate(password_dictionary[service]):
            if user == username:
                del password_dictionary[service][i]
                user_found = True
                print(f"Account {username} was removed from service: {service}")
                break
            if not user_found:
                print(f"User{username} wasn't found in {service}")
    else:
        print(f"Service {service} wasn't found in dictionary") 
           
# change password

def change_password(service, username, new_password):
    if service in password_dictionary:
        for i, (user, _) in enumerate (password_dictionary[service]):
            if user == username:
                password_dictionary[service][i] = (username, new_password)
                print(f"Password fore password {username} in service {service} was changed")
                return
        print(f"Account {username} doesn't exist in service {service}")
    else:
        print(f"{service} doesn't exist")

# list passwords

def list_passwords():
    if password_dictionary:
        print("Saved services")
        for service in password_dictionary:
            print(f"- {service}")
    else:
        print("There are no services yet")

