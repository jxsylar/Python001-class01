# -*- coding: utf-8 -*-

import functools
import threading
import time
from typing import Callable, Iterable


"""
扁平序列: 只能容纳一种类型

可变性(mutable): 可以在其 `id()` 值保持固定的情况下改变其取值, 即可以在原位置修改对象的值.
不可变性(immutable): 在其 `id()` 值保持固定的情况下不可改变其值, 即不能在原位置修改对象的值.

可变序列: 具有可变性(mutable)的对象
不可变序列: 具有不可变性(immutable)的对象

+-------------------+----------+----------+
|      容器序列      |  扁平序列  | 可变序列  |
+-------------------+----------+----------+
|        list       |    ×     |    √     |
|       tuple       |    ×     |    ×     |
|        str        |    √     |    ×     |
|       dict        |    ×     |    √     |
| collections.deque |    ×     |    √     |
+-------------------+----------+----------+
"""


def my_map(func: Callable, iterables: Iterable):
    """ 自定义一个 python 函数, 模拟 map 函数的功能 """
    if hasattr(iterables, '__iter__'):
        for i in iterables:
            yield func(i)
    else:
        raise TypeError(f"'{iterables.__class__.__name__}' object is not iterable")


def timeit(func):
    @functools.wraps(func)
    def wrap(*args, **kwargs):
        fun_name = str(func.__name__)
        tic = time.perf_counter()
        ret = func(*args, **kwargs)
        toc = time.perf_counter()
        print(f"{fun_name}: Time elapse(s): {toc - tic}")
        return ret

    return wrap


def target(second):
    print(f"{'-' * 20}{threading.current_thread().name}, {threading.active_count()} running{'-' * 20}")
    print(f"{threading.current_thread().name}: sleep {second}s")
    time.sleep(second)
    print(f"{'-' * 20}{threading.current_thread().name}, {str(threading.active_count())} ended{'-' * 20}")
    return second


@timeit
def case(num):
    print(f"{threading.current_thread().name:=^60}")
    threads = list()
    for i in range(num):
        t = threading.Thread(target=target, args=[i], name='Thread 直接创建子线程')
        threads.append(t)
        t.start()
    for i in threads:
        i.join()
    print(f"{threading.current_thread().name:=^60}")


if __name__ == '__main__':
    try:
        for i in my_map(lambda x: x ** 5, 3):
            print(i)
    except TypeError as e:
        print(e)

    for i in my_map(lambda x: x ** 3, range(5)):
        print(i)

    case(10)
