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

ants：problem5
对列表进行切片操作s[:]或者list(s)会进行**浅拷贝**，切片操作 self.place.bees[:] 创建了一个新的列表，这个列表中的每个元素都是原始列表中 Bee 实例的引用。也就是说，虽然新列表的结构与原始列表无关（例如在新列表中添加或删除元素不会改变原列表），但列表中存储的对象依然是同样的 Bee 实例，因此，当你在迭代 bees 列表时对 i 进行操作（例如调用 i.reduce_health(...)），实际上是修改了原始 Bee 实例的内部状态，从而导致原列表中的相应对象状态发生变化。
在 Python 中，如果在遍历一个列表的同时对该列表进行修改（比如删除或添加元素），会导致迭代器内部使用的索引和列表的实际状态不同步，从而可能跳过某些元素或导致意外的行为。例如，当你从列表中删除某个元素时，后面的元素会向前移动，而迭代器同时又会增加索引，这样就可能导致某个本应被处理的元素被跳过，或是出现其他逻辑错误。因此，为了避免这种情况，我们通常会先对列表创建一个浅拷贝，然后再对拷贝进行遍历，而修改原始列表。这样既能避免因为迭代过程中的列表结构变化而遗漏元素的问题，也可以保持程序行为的可预测性

super() 返回一个代理对象，用于访问父类的方法
super().__init__(health) 会自动传入 self。在 Python 中，当你在类的方法内使用 super() 时，它会自动把当前实例（self）作为第一个参数传递给父类的方法。