def peek_sum(x, y):
    print 'Adding ', x, ' and ', y
    return x + y


print reduce(peek_sum, [1, 2, 3, 4, 5])
