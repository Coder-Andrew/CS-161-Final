def create_account():
    name = input("\nEnter a name for the account: ")
    password = input("Enter a password for the account: ")
    return [name,password,0]

def check_credentials(user_list, retry_message):
    while True:
        user_input = input

users = []

while True:
    choice = input("{:-^16s}\n\n(1) Login\n(2) Create account\n".format("Menu"))
    
    if choice == "2":
        users.append(create_account())
        print("Account created! Please login from the main screen!\n")

    elif choice == "1":
        is_in = 0
        
        user_name = input("Please enter your user name: ")
        
        for i in range(len(users)):
            if user_name == users[i][0]:
                user_index = i
                is_in = 1
                break
            
