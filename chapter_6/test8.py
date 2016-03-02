def hello_1(greeting, name):
    print '%s, %s!' % (greeting, name)


def hello_2(name, greeting):
    print '%s, %s!' % (name, greeting)


def hello_3(greeting='Hello', name='world'):
    print '%s, %s!' % (greeting, name)


print hello_1('Hello', 'world')
print hello_2('Hello', 'world')

print hello_1(greeting='Hello', name='world')
print hello_1(name='world', greeting='Hello')

print hello_2(greeting='Hello', name='world')

print hello_3()
print hello_3('Greetings')
print hello_3('Greetings', 'universe')

print hello_3(name='Gumby')

params = {'name': 'Sir Robin', 'greeting': 'well met'}
print hello_3(**params)
