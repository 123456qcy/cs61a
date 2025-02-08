### 已完成
+ hw01
+ hw02
+ hw03 Q6匿名函数递归想不出来
+ hw04
+ hw05 Q3 yield_paths
+ lab01
+ lab02
+ lab03
+ lab04 Q3 buy
+ lab05
+ lab06
+ hog
+ cats P7 minimum_mewtations


### study
+ memo函数使用缩短时间提升效率
``` python
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

#使用示例
fib = memo(fib)
fib(100)
```