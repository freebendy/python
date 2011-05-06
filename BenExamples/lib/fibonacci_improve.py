previous = {0:1, 1:1}
def fibonacci_improve(n):
    if previous.has_key(n):
        return previous[n]
    else:
        newValue = fibonacci_improve(n-1) + fibonacci_improve(n-2)
        previous[n] = newValue
        return newValue
