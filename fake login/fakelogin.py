import time

musername = input('Add a user name : ')
mpassword = input('Add a password : ')

print('Done Saved!')

username = input('Enter the user name : ')
password = input('Enter the password : ')

if musername == username and mpassword != password:
    print('Username is wrong check username')
elif mpassword == password and musername != username:
    print('Password incorrect, Check password')
elif mpassword == password and username == musername:
    print('Done! Login now')
    time.sleep(5)
    print('Hi')
    time.sleep(10)
    print('Welcome to the system')

else:
    print('Unexpected error')



