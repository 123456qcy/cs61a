def fib(n):
    if n == 1 or n == 0:
        return n
    else:
        return fib(n - 2) + fib(n - 1)#此处的fib函数调用的是替换后的memorized函数
def memo(f):
    cache = {}
    def memorized(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]
    return memorized#用来替换的memorized函数必须与原函数同名才可以节省时间
