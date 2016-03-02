def with_stars(**kwds):
    print kwds['name'], ' is ', kwds['age'], ' years old'


def without_stars(kwds):
    print kwds['name'], ' is ', kwds['age'], ' years old'


args = {'name': 'Mr. Gumby', 'age': 42}

print with_stars(**args)
print without_stars(args)
