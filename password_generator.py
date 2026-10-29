#password generator after 5 seconds
import time
import random
import string

def passwords():
    while True:
        password =''.join(random.choices((string.ascii_letters + string.digits), k=10))
        print(f'''your password is:
{password}  ''')
        print('password changing in: ')
        for x in range(5, 0, -1):
            print(x, end='')
            time.sleep(1)
        print(' \n')
passwords()
