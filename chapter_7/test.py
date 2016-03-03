class Secretive:
    def __inaccessible(self):
        print 'Bet you can not see me...'

    def accessible(self):
        print 'The secretmessage is : '
        self.__inaccessible()


s = Secretive()
# s.__inaccessible()
s.accessible()
print Secretive._Secretive__inaccessible
print s._Secretive__inaccessible()
