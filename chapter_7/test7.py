class Calculator:
    def calculate(self, expression):
        self.value = eval(expression)


class Talker:
    def talk(self):
        print 'Hi, my value is ', self.value


class TalkingCalculator(Calculator, Talker):
    pass


tc = TalkingCalculator()
tc.calculate('1 + 2 * 3')
tc.talk()

print hasattr(tc, 'talk')
print hasattr(tc, 'fnod')

print callable(getattr(tc, 'talk', None))
print callable(getattr(tc, 'fnord', None))

setattr(tc, 'name', 'Mr. Gumby')
print tc.name