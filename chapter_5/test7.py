name = ''

# while not name or name.isspace():
while not name.strip():
    name = raw_input('Please enter your name : ')
    print 'Hello %s!' % name
