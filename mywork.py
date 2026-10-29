#creating unique username and password
def create_account():
    creating =True
    while creating:
        account={''}
        user=input('Sign in / create new account: ').lower()
        if user =='sign in':
            log_in=input('enter your username: ').lower()
            if log_in in account:
                password =input('enter your password: ')
                if password ==account.get(log_in):
                    print('Log in Successful')
                    print(f'welcome Back {log_in}')
                    creating= False
                elif password != account.get(log_in):
                    while password != account.get(log_in):
                        print('wrong password')
                        password= input('enter your password: ')
                    else:
                        if password == account.get(log_in):
                            print(f'''log in successful
welcome Back {log_in}''')
                    creating= False
            elif log_in not in account:
                while log_in not in account:
                    print('unknown username')
                    log_in = input('enter your username: ').lower()
                    if log_in in account:
                        password =input('enter your password: ')
                        if password ==account.get(log_in):
                            print('Log in Successful')
                        elif password != account.get(log_in):
                            while password != account.get(log_in):
                                print('Wrong Password')
                                password= input('enter your password: ')
                            else:
                                print(f'''log in successful
welcome Back {log_in}''')
                            creating= False
        elif user =='create new account':
            create= input('choose a username: ').lower()
            while create in account:
                print('username already exists')
                create = input('enter a username: ').lower()
            else:
                new=input('choose a strong password: ')
                confirm=input('confirm your password: ')
                while new != confirm:
                    print('passwords do not match')
                    new = input('choose a strong password: ')
                    confirm = input('choose a strong password: ')
                else:
                    print('account created successfully')
                creating= False
            account.update({create: new})
            print(account)
        else:
            print('invalid input')
