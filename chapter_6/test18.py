def multiplier(factor):
    def multiplyByFactor(number):
        return number * factor

    return multiplyByFactor


double = multiplier(2)
print double(5)

triple = multiplier(3)
print triple(3)

print multiplier(5)(4)
