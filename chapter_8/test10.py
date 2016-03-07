def describePerson(person):
    print 'Description of ', person['name']
    print 'Age : ', person['age']
    if 'occupation' in person:
        print 'Occupation ', person['occupation']
