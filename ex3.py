i=0
while i in range(2):
    username=input('enter username: ')
    password=input('enter password: ')
    if username=='admin' and password=='1234':
        print('Access granted')
    else:
        print('Access denied')
    i=i+1