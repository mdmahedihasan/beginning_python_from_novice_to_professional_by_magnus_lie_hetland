def peek_max(x, y):
    print 'Finding max of ', x, ' and ', y
    return max(x, y)


print reduce(peek_max, [3, 5, 2, 6, 9, 2])
