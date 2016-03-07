class Bird:
    def __init__(self):
        self.hungry = 1

    def eat(self):
        if self.hungry:
            print 'Aaaahh...'
            self.hungry = 0
        else:
            print 'No, thanks'


class SongBird(Bird):
    def __init__(self):
        Bird.__init__(self)
        self.sound = 'Squawk!'

    def sing(self):
        print self.sound


b = Bird()
b.eat()
b.eat()
b.eat()

sb = SongBird()
sb.sing()
sb.eat()
sb.eat()