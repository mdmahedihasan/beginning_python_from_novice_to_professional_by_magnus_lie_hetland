class Filter:
    def init(self):
        self.blocked = []

    def filter(self, sequence):
        return [x for x in sequence if x not in self.blocked]


class SPAMFilter(Filter):
    def init(self):
        self.blocked = ['SPAM']


f = Filter()
f.init()
print f.filter([1, 2, 3])

s = SPAMFilter()
s.init()
print s.filter(['SPAM', 'SPAM', 'SPAM', 'SPAM', 'eggs', 'bacon', 'SPAM'])

print issubclass(SPAMFilter, Filter)
print issubclass(Filter, SPAMFilter)

print SPAMFilter.__bases__
print Filter.__bases__

s = SPAMFilter()
print isinstance(s, SPAMFilter)
print isinstance(s, Filter)
print isinstance(s, str)

print s.__class__