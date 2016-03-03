class Class:
    def method(self):
        print 'I have a self...'


def function():
    print 'I do not...'


instance = Class()
instance.method()

instance.method = function
instance.method()