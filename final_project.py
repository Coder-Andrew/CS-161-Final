#**************************************
#
# a program that lets you charge accounts and make payments
#
#@author AE
#@version CS 161 Final 6/7/2021
#**************************************

def admin_menu(choice): #sets up the admin menu and options, takes a choice as input
    if choice == "1":
        ATM.print_accounts()

    elif choice == "2":
        user = input("Enter the username whose information you'd like to display: ")
        ATM.print_account(user)
                                    
    elif choice == '3':
        ATM.admin_remove_all_accounts()

    elif choice == '4':
        user = input("Enter the account you'd like to close: ")
        ATM.delete_account(user)

    return choice

class Bank: #class that sets up bank
    def __init__(self, name): #takes a name by default
        self.__accounts = []
        self.__accounts.append(["admin","admin","1000000"]) #creates admin account by default using list method     username: admin         password: admin
        self.__name = name

    def __str__(self):
        return ("{} Banking Software".format(self.__name))

    def add_account(self, user_name, password, initial_balance):    #method that adds accounts
        self.__accounts.append([user_name, password, initial_balance, {}])

    def print_accounts(self):   #prints all account info
        for j in range(1,len(self.__accounts)):
            print("Username: {}\nPassword: {}\nBalance: ${:.2f}\nCharges: {}\n".format(self.__accounts[j][0], self.__accounts[j][1], self.__accounts[j][2], self.__accounts[j][3]))

    def print_account(self, username):  #prints a single account
        isuser = -1
        for i in range(len(self.__accounts)):
            if self.__accounts[i][0] == username:
                print("\nUsername: {}\nPassword: {}\nBalance: ${:.2f}\nCharges: {}\n".format(self.__accounts[i][0], self.__accounts[i][1], self.__accounts[i][2], self.__accounts[i][3]))

    def print_account_charges(self, username):  #prints the charges that an account has
        user_index = -1
        for i in range(len(self.__accounts)):
            if self.__accounts[i][0] == username:
                user_index = i

        for key in self.__accounts[user_index][3]:
            print("Charge of ${:.2f} from {}".format(self.__accounts[user_index][3][key], key))

        if len(self.__accounts[user_index][3]) == 0:
            print("No charges found")

    def print_account_balance(self, username):  #prints account's balance
        user_index = -1

        for i in range(len(self.__accounts)):
            if self.__accounts[i][0] == username:
                user_index = i
                break
        return("Balance: ${}".format(self.__accounts[user_index][2]))

    def login(self, user_name, password):   #login method that returns -1 if login is unsuccessful 
        for i in range(len(self.__accounts)):
            if self.__accounts[i][0] == user_name and self.__accounts[i][1] == password:
                user_index = i
                print("Successfully logged in as: {}".format(user_name))
                return user_index
            
        print("Username or password were incorrect, please try again!")
        return -1

    def delete_account(self, user_name):    #lets the admin delete accounts
        for i in range(len(self.__accounts)):
            if self.__accounts[i][0] == user_name:
                print("Account removed successfully!")
                self.__accounts.pop(i)
                return 1

        print("Account not found/invalid username/password. Please try again!")
        return 0

    def charge_account(self, charging_account, charged_account, amount):    #lets users charge other users
        if amount < 1:
            return "Cannot charge negative or 0 money"
        
        charging_account_index = -1
        charged_account_index = -1
        accounts_exist = 0

        for i in range(len(self.__accounts)):
            if charging_account in self.__accounts[i]:
                charging_account_index = i
            if charged_account in self.__accounts[i]:
                charged_account_index = i

        if charging_account_index == -1 and charged_account_index == -1:
            print("\nNeither account found\n")
        elif charging_account_index == -1:
            print("\nCharging account not found\n")
        elif charged_account_index == -1:
            print("\nCharged account not found\n")
        else:
            accounts_exist = 1

        if charging_account not in self.__accounts[charged_account_index][3] and accounts_exist == 1:
            self.__accounts[charged_account_index][3][charging_account] = 0

        if accounts_exist == 1:
            self.__accounts[charged_account_index][3][charging_account] += amount

    def pay_charge(self, home_account, charger_account, amount):    #lets users pay charges
        if amount < 1:
            return "Cannot pay negative money or 0 money"

        home_account_index = -1
        for i in range(len(self.__accounts)):
            if self.__accounts[i][0] == home_account:
                home_account_index = i

        if home_account_index == -1:
            print("Home account not found!")

        if charger_account not in self.__accounts[home_account_index][3]:
            print("Charges from charger not found")

        else:
            self.__accounts[home_account_index][3][charger_account] -= amount
            self.__accounts[home_account_index][2] -= amount

    def admin_remove_all_accounts(self):    #deletes all accounts
        self.__accounts = {}


ATM = Bank("Western Bank")  #initializing the bank with the name Western Bank


ATM.add_account("Bob","bobby",500)  #adding a block of users 
ATM.add_account("Andy","PI",600)
ATM.add_account("Mary","fly",1000)
ATM.add_account("Tim","2",2222)

ATM.charge_account("Andy","Mary",100) #adds a couple charges to Mary
ATM.charge_account("Bob","Mary",50)

while True: #entering main menu login loop
    choice = input("\n\n{:-^16s}\n\n1.) Login\n2.) Create Account\n3.) Quit\n\nChoice: ".format("Menu"))    #menu print statement
    
    if choice == '3':   #quit branch
        break

    if choice == '2':   #create account branch
        username = input("\nEnter a username for the account: ")
        password = input("Enter a password for the account: ")
        balance = input("Enter the amount of money you would like to put into your account (as an integer): ") 
        while balance.isdigit() == False:   #using string method to test if 
            balance = input("Please enter a valid number for the initial balance!: ")
        balance = int(balance)   
        ATM.add_account(username, password, balance)
        print("Account created! Please login from the main menu!")

    if choice == '1':   #login branch
        username = input("\nEnter your username: ")
        password = input("Enter you password: ")

        users_index = ATM.login(username, password)
        while users_index == -1:
            print("Or enter -1 in one of the fields to quit")
            username = input("\nEnter your username: ")
            if username == "-1":
                break
            password = input("Enter you password: ")
            if password == "-1":
                break

            users_index = ATM.login(username, password) #attempts login using instance method

        while True: #entering loop for user's choices
            if username != "admin": #checks to see if the user is admin
                
                print("\n\nHello {}! What would you like to do?\n\n{}\n\n1.) View charges\n2.) Pay charge\n3.) Charge someone\n4.) Quit".format(username, ATM.print_account_balance(username)))
                choice = input("\nChoice: ")

                if choice == "1":
                    ATM.print_account_charges(username)

                elif choice == "2":
                    charger = input("Enter the name of the person you would like to pay: ")
                    amount = int(input("Enter the amount you would like to pay: "))
                    ATM.pay_charge(username, charger, amount)

                elif choice == "3":
                    chargee = input("Enter the name of the person you would like to charge: ")
                    amount = int(input("Enter the amount you would like to charge {}: ".format(chargee)))
                    ATM.charge_account(username, chargee, amount)

                elif choice == "4":
                    break

            else:   #admin menu.        username: admin    password: admin

                
                
                print("\nHello admin! What would you like to do?\n\n1.) Print all account information\n2.) Print individual's account information\n3.) Remove all accounts\n4.) Delete account\n5.) Quit")
                choice = input("\n\nChoice: ")
                
                admin = admin_menu(choice) #using the admin menu function

                if admin == '5':
                    break
                
    else:
        print("Invalid choice, please try again!")

