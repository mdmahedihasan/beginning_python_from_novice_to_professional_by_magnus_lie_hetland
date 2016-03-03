class Person:
    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def greet(self):
        print "Hello, world! I am %s." % self.name

foo = Person()
bar = Person()
foo.setName('Luke SkyWalker')
bar.setName('Anakin SkyWalker')
foo.greet()
bar.greet()

print foo.name
bar.name = 'Yoda'
bar.greet()