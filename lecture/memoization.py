def count(f):
    def countt(n):
        countt.count_ += 1
        return f(n)
    countt.count_ = 0
    return countt

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-2) + fib(n-1)

def memo(f):
    cache = {}
    def func(n):
        if n in cache:
            return cache[n]
        else:
            cache[n] = f(n)
            return cache[n]
    return func
