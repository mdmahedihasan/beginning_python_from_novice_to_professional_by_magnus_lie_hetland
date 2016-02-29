database = [
    ['albert', '1234'],
    ['dilbert', '4242'],
    ['smith', '7524'],
    ['jones', '9843']
]

userName = raw_input("User Name : ")
pin = raw_input("Pin Code : ")

if [userName, pin] in database:
    print 'Access granted!'
else:
    print 'wrong'
