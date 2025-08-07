users = {
    'mahdi': '1385',
    'reza' : '1234',
    'amir' : '9876',
    'zahra' : "zm1374"
    'and .........'
} # Database

inter_username = input("Please enter your username: ")

inter_password = input('Please enter your password:')

# if inter_username in users and users[inter_username] == inter_password :
#     print('welcome to my saits ')

while inter_username not in users or inter_password != users[inter_username] :
    print('')
    print('Username does not match the password')
    inter_username = input(" Please enter your username again : ")
    inter_password = input(' Please Enter your password again :')

print('You successfully arrived.' \
'Welcome')


 
