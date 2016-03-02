def hello_4(name, greeting='Hello', punctuation='!'):
    print '%s, %s%s' % (greeting, name, punctuation)


print hello_4('Mars')
print hello_4('Mars', 'Howdy')
print hello_4('Mars', 'Howdy', '...')
print hello_4('Mars', punctuation='.')
print hello_4('Mars', greeting='Top of the morning to ya')
print hello_4()
