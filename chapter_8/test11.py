def describePerson(person):
    print 'Description of ', person['name']
    print 'Age ', person['age']
    try:
        print 'Occupation ', person['occupation']
    except KeyError:
        pass
