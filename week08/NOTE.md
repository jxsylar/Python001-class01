- [Python 的对象类型](#python-的对象类型)
  - [一. Python 知识结构](#一-python-知识结构)
  - [二. 为什么要使用内置类型](#二-为什么要使用内置类型)
  - [三. Python 核心数据类型](#三-python-核心数据类型)
  - [四. 可变对象和不可变对象](#四-可变对象和不可变对象)
  - [五. 小结](#五-小结)
- [动态类型](#动态类型)
  - [一. 缺少声明语句](#一-缺少声明语句)
    - [变量, 对象和引用](#变量-对象和引用)
    - [类型属于对象, 而不是变量](#类型属于对象-而不是变量)
    - [对象的垃圾回收](#对象的垃圾回收)
  - [二. 共享引用](#二-共享引用)
    - [不可变对象的共享引用](#不可变对象的共享引用)
    - [可变对象的共享引用](#可变对象的共享引用)
    - [对象复制(copy)](#对象复制copy)
    - [缓存机制](#缓存机制)
    - [相等判断](#相等判断)
  - [四. "弱"引用](#四-弱引用)
  - [五. 小结](#五-小结-1)
- [装饰器](#装饰器)
  - [一. 前言](#一-前言)
  - [二. 函数的特点](#二-函数的特点)
  - [三. 什么是装饰器](#三-什么是装饰器)
    - [装饰器还原](#装饰器还原)
  - [四. 内置装饰器](#四-内置装饰器)
  - [五. 装饰器的作用](#五-装饰器的作用)
- [可迭代对象, 迭代器, 生成器](#可迭代对象-迭代器-生成器)


# Python 的对象类型



## 一. Python 知识结构


在 Python 中, **一切皆对象**, 对象有**属性**和**方法**. 对象是 Python 中最基本的概念, 本文将全面介绍 Python 的内置对象类型.(关于对象的详细细节, 请阅读后面关于**类**的相关章节.)


在接触代码之前, 先了解一下 Python 的全貌: Python 程序可以分解为模块, 语句, 表达式和对象. 如下所示:


1. 程序由模块构成
1. 模块包含语句
1. 语句包含表达式
1. 表达式创建并处理对象



## 二. 为什么要使用内置类型


与一些较低层语言(如 c/c++)不同, Python 提供了强大的对象类型作为语言的组成部分, 因此大部分情况下无需自己实现, 直接使用即可, 除非你有内置类型都无法处理的特殊对象. 使用内置对象有以下优势:


1. 内置对象是语言标准的一部分, 使用它们使程序更易编写和阅读. 对于大部分任务, 内置对象完全可以胜任.
1. 内置对象是可扩展的组件. 对于较复杂的任务, 仍然可以使用类来拓展自定义对象类型.
1. 内置对象往往比定制的数据结构更有效率. 在速度方面, Python 的内置类型使用了已优化的 C 实现的数据结构来加速.



## 三. Python 核心数据类型


Python 的内置对象和示例如下表所示:



| 对象类型 | 字面量(literal)/构造示例 |
| :---: | :---: |
| 数字 | `1234`, `3.1415,` `3+4j`, `0b1111`, [`Decimal()`](https://docs.python.org/zh-cn/3/library/decimal.html#decimal.Decimal), [`Fraction()`](https://docs.python.org/zh-cn/3/library/fractions.html#fractions.Fraction) |
| 字符串 | `'spam'`, `"Bob's"`, `b'a\x01c'`, `u'sp\xc4m'` |
| 列表 | `[1, [2, 'three'], 4.5]` , `list(range(10))`  |
| 字典 | `{food': 'spam', 'taste': 'yum'}` , `dict(hours=10)`  |
| 元组 | `(1, 'spam', 4, 'u')` , `tuple('spam')` , [`namedtuple`](https://docs.python.org/zh-cn/3/library/collections.html#collections.namedtuple)  |
| 集合 | `set('abc')` , `{'a', 'b', 'c'}`  |
| 文件 | `open('test.txt')`  |
| 其他核心类型 | 布尔类型, None |
| 程序单元类型 | 函数, 模块, 类 |
| Python 实现相关类型 | 已编译代码, 调用栈跟踪 |



在 Python 中, **没有类型声明**, 运行的表达式的语法决定了创建和使用的对象的类型. 一旦创建了一个对象, 它就和操作集合绑定了: 你只能对字符串进行字符串相关操作; 对列表进行列表相关的操作. 用更规范的术语描述, Python 是**动态类型**的(它自动地跟踪类型而不是声明的代码), 同时, Python 也是**强类型**语言(你只能对一个对象进行适合该类型的有效操作, 很少做隐式类型转换). 



举个例子:


强类型: 


```python
>>>  1 + '1'  # 不会做隐式类型转换, 因此会报错
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'
```


弱类型:


```javascript
> 1+'1'  // 数字 1 隐式转换为字符串 1. 有做隐式类型转换
"11"
```


动态类型:


```python
>>> a = 1
>>> type(a)
<class 'int'>
>>> a = '1'
>>> type(a)
<class 'str'>
```


静态类型:


```java
int a=1
```


## 四. 可变对象和不可变对象


在 Python 中, **一切皆对象**. 数字是对象, 字符串是对象, 列表是对象, 元组是对象, 函数是对象, 类是对象, 模块是对象, 包也是对象, 总之, 一切皆对象. 


那么问题来了, 什么是对象? 


[对象(object)](https://docs.python.org/zh-cn/3/reference/datamodel.html#objects-values-and-types):


1. 对象是 Python 中对数据的抽象.  Python 程序中的所有数据都是由对象或对象间关系来表示的.  (从某种意义上说, 按照冯・诺依曼的 "存储程序计算机" 模型, 代码本身也是由对象来表示的. )
1. 每个对象都有各自的编号, 类型和值. 一个对象被创建后, 它的编号就绝不会改变; 你可以将其理解为该对象在内存中的地址.   [`id()`](https://docs.python.org/zh-cn/3/library/functions.html#id) 函数能返回一个代表其编号的整型数. 编号相同时, 表示都指向同一块内存空间.



具体而言, 每一个对象都有两个标准的头部信息:


1. 类型标志符(type designator): 标志这个对象的类型. 可以使用 [`type()`](https://docs.python.org/zh-cn/3/library/functions.html#type) 函数查看对象的类型.
1. 引用计数器(reference counter): 记录着这个对象被引用的次数, 这个在下一篇文章会详细讲解.



根据对象能否在 `[id()](https://docs.python.org/zh-cn/3/library/functions.html#id)` 保持固定的情况下改变其值, Python 对象可为**可变对象**和**不可变对象**.


在讲**可变对象**和**不可变对象**之前, 需要知道**可变性 (**[**mutable**](https://docs.python.org/zh-cn/3/glossary.html#term-mutable)**)和不可变性(**[**immutable**](https://docs.python.org/zh-cn/3/glossary.html#term-immutable)**)**:


根据对象在创建后能不能在原位置(in place)改变, 分为:


- 可变性([mutable](https://docs.python.org/zh-cn/3/glossary.html#term-mutable)): 可以在其 [`id()`](https://docs.python.org/zh-cn/3/library/functions.html#id) 值保持固定的情况下改变其取值, 即可以在原位置修改对象的值.
- 不可变性([immutable](https://docs.python.org/zh-cn/3/glossary.html#term-immutable)): 在其 [`id()`](https://docs.python.org/zh-cn/3/library/functions.html#id) 值保持固定的情况下不可改变其值, 即不能在原位置修改对象的值.




- 可变对象: 具有可变性的对象. 包括列表, 字典, 集合等.
- 不可变对象: 具有不可变性的对象. 包括**数字(如整数 int, 浮点数 float), 字符串(string)和元组(tuple)**. 这样的对象不能被改变. **如果必须存储一个不同的值, 则必须创建新的对象**. 它们在需要常量哈希值的地方起着重要作用, 例如作为字典中的键.



上面的概念有点抽象, 下面举个例子来说明:

```python
>>> # 可变对象, 以列表 list 为例, 关于列表的详细用法, 请阅读后面关于列表的相关章节
>>> a = []
>>> id(a)
2683484540480
>>> a.append(1)
>>> a   # a 的值改变了
[1]
>>> id(a)
2683484540480  # id() 值没变化
>>> a[0] = 2   # 再次修改列表里第一个元素的值
>>> a
[2]
>>> id(a)
2683484540480  # id() 值依旧没变化, 即列表可以在 id() 值不变的情况下修改其值
```


```python
>>> # 不可变对象, 以字符串为例, 关于字符串的详细用法, 请阅读后面关于字符串的相关章节
>>> s = 'abc'
>>> id(s)
2683475704560
>>> s[0] = 'A'  # 修改第一个字符会报错, 因为字符串不能在原对象里修改
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
>>> s = 'Abc'  # 若想存储一个不同的值, 则必须创建新的对象
>>> id(s)
2683484497136  # id() 值改变了, s 引用了新的对象, 详情请阅读下一章节: 动态类型
```


## 五. 小结


Python 提供的内置数据类型不仅能让编程变得更简单, 而且它们更强大和更有效. 同时, 理解可变对象和不可变对象的特征, 是深入理解动态类型, 赋值语句等行为的基础.


# 动态类型



动态类型以及由它提供的多态性, 是 Python 语言简洁性和灵活性的基础.


> 1. 动态类型: 定义变量或参数时, 不需要声明变量或参数的数据类型. 相对应的是静态类型.
> 1. 多态性: 不同类型的对象进行相同的操作时, 它会根据对象类型的不同而表现出不同的行为. 即这个操作有着"多种形式", 具体的表现由对象的类型决定.



## 一. 缺少声明语句


在 Python 中, 类型是在**运行时**自动决定的, 而不是通过代码声明. 这意味着没有必要事先声明变量(或对象)的数据类型.


这就是 Python 语言的**动态类型**模型.


### 变量, 对象和引用


在 Python 里, 运行下面赋值语句:


```python
>>> a = 3
```


之后, 就可以将 `a` 作为一个变量来使用, 这是一种非常自然的方式:


1. 变量创建: 一个变量(即变量名), 就像 `a`, 当代码第一次给它赋值时就创建了它. 如果后面再次给 `a` 赋值, 则会改变已经创建的变量名的值. 在 Python 代码运行之前会先检测变量名.
1. 变量类型: 变量永远不会拥有任何和它关联的类型信息或约束. 类型的概念只存在于**对象**而不是变量名中. 变量是通用的, 它只是在一个特定时间点, 简单地**引用**了一个特定的**对象**而已.
1. 变量使用: 当变量出现在表达式中时, 它会马上被当前**引用的对象**所替代, 无论这个对象是什么类型. 此外, 所有的变量在使用之前必须被明确地赋值, 否则, 使用未被赋值的变量会产生错误.



```python
>>> data  # 使用未被赋值的变量会产生错误
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'data' is not defined
```


上面的赋值语句 `a = 3` , Python 将会执行下面三个动作:


1. 创建一个对象来代表值 `3`.
1. 如果变量 `a` 没有创建, 则会创建一个变量 `a`.
1. 将变量与新的对象 `3` 相连接.



![image.png](https://cdn.nlark.com/yuque/0/2020/png/267146/1591380803847-2f5adfe1-e10f-42a6-87ed-9880c4a8ce72.png#align=left&display=inline&height=319&margin=%5Bobject%20Object%5D&name=image.png&originHeight=638&originWidth=1049&size=39507&status=done&style=shadow&width=524.5)






总而言之, 理解动态特性, 需要清楚地将**变量名**和**对象**划分开: **变量总是连接到对象, 并且一个对象可以连接到另一个对象**.


> **赋值语句是在目标和对象之间建立绑定(bindings)关系**. 通俗而言就是建立一个对象的别名.



在 Python 中, **一切皆对象**. 数字是对象, 字符串是对象, 列表是对象, 元组是对象, 函数是对象, 类是对象, 模块是对象, 包也是对象, 总之, 一切皆对象.


从变量到对象的连接称作**引用**. 引用是一种关系, 通过内存中的指针的形式来实现, 一旦使用(引用)变量, Python 会自动跟踪这个变量到对象的连接:


1. 变量是一个系统表的入口, 包含了指向对象的连接.
1. 对象是被分配到的一块内存, 有足够的空间去表示它们所代表的值.
1. 引用是自动形成的从变量到对象的指针.



从概念上讲, 每一次通过运行一个表达式会生成一个新的对象, Python 都会开辟一块新的内存空间来存储这个对象. 如果多次重复创建相同的对象, 岂不是很浪费内存, 因此, 作为一种优化手段, Python 缓存了**不可变对象**(如小的整数, 字符串)并对其进行复用, 这样, 如果多次重复创建同一个**不可变对象**, 这些对象都指向同一个内存地址. 


![image.png](https://cdn.nlark.com/yuque/0/2020/png/267146/1591382465065-019e304c-7402-4154-9682-44349b852dfa.png#align=left&display=inline&height=400&margin=%5Bobject%20Object%5D&name=image.png&originHeight=799&originWidth=997&size=53227&status=done&style=shadow&width=498.5)


实际上, 对象不仅有足够的空间来表示它的值, 还包含了更复杂的结构. 每一个对象都有两个标准的头部信息:


1. 类型标志符(type designator): 标志这个对象的类型. 使用 [`type()`](https://docs.python.org/zh-cn/3/library/functions.html#type) 查看对象的类型.
1. 引用计数器(reference counter): 记录着这个对象被引用的次数, 引用计数器决定何时释放这个对象, 从而回收内存空间. 使用 [`sys.getrefcount(object)`](https://docs.python.org/zh-cn/3/library/sys.html#sys.getrefcount) 查看对象被引用的次数.



```python
>>> a = 1
>>> id(a)  # 查看 a 引用的对象的唯一编号
140725852362400
>>> type(a)  # 查看 a 引用的对象类型
<class 'int'>
>>> import sys
>>> sys.getrefcount(a)  # 查看 a 引用次数, 注意, 运行这条语句时, 也是引用 a, 因此, 会比预期多 1
667   # 为什么结果这么大? 因为绝大多数都是 IDLE 系统代码所使用的, 而非自己的代码
```


### 类型属于对象, 而不是变量


变量名没有类型, 类型属于对象, 而不是变量名. 当同一个变量名被不同的对象多次赋值时, 只是让变量引用了其相对应类型的对象而已. 因为, Python 的变量就是在特定的时间引用了一个特定的对象.


假如有下面例子:


```python
>>> a = 3
>>> a = 'spam'
>>> a = 1.23
```


每次赋值, 只是把变量 `a` 修改为相应对象的引用(修改变量名与对象的绑定关系). 每次修改变量 `a` 引用的对象时, `a` 都知道所引用对象的类型:


```python
>>> a = 3
>>> type(a)
<class 'int'>
>>> a = 'spam'
>>> type(a)
<class 'str'>
>>> a = 1.23
>>> type(a)
<class 'float'>
```


这是因为对象知道自己的类型, 每个对象都包含一个头部信息, 其中标记了这个对象的类型. 如: 整数对象 `3`, 包含了值 `3` 和一个标志符, 告诉 Python 这是一个整数对象(一个指向 int 的对象的指针); 字符串对象 `'spam'` 则指向了一个 `str` (字符串类型) 的指针. 对象记录了它们各自的类型, 变量就没必要重复再记录了.


总之, **类型与对象相关联, 而不是和变量关联**. Python 能够知道每个**变量引用对象的类型**(后续我们简称为**变量的类型**), 因此我们需要关心的是每一种对象支持什么样的操作.


### 对象的垃圾回收


在前面的例子中, 我们把不同类型的对象赋值给变量 `a`, 但是当重新给变量 `a` 赋值时, 它前一个引用值发生了什么变化? 即: 当运行了 `a = 'spam'` , 那么前面的 `3` 发生了什么变化?


前面讲到: 每一个对象都有两个标准的头部信息, 一个是类型标志符, 一个是引用计数器. 每当一个变量名被赋予了一个新的对象时, 如果原来的对象没有被其他的变量名或对象所引用的话, 那么之前的那个对象占用的空间就会被回收, 这种回收对象空间的技术叫垃圾回收(**G**arbage **C**ollection, GC). 正是因为有垃圾回收的技术, 内存空间才得以重复利用, 否则内存终会枯竭.


> 垃圾回收: 将已经终止生命周期的变量占用的内存给释放掉, 这是一种内存管理技术. 参考: [什么是编程语言的垃圾回收机制?](https://www.zhihu.com/question/19831128)



实际上, 每种编程语言都有垃圾回收技术, 只不过具体实现方式会有所差异, 但原理是一样的. 有些编程语言的垃圾回收需要程序员负责, 如 C/C++; 有些编程语言是在虚拟机层面实现垃圾回收, 如: Java, 这种是虚拟机帮你实现了, 大部分情况下程序员专注于业务代码就好了, 大大降低了内存泄露的风险, 当然, 程序员也可以主动进行垃圾回收; 而 Python 语言, 垃圾回收在是在 Python 解释器里实现的, 程序员无需负责垃圾回收, Python 会在适当的时候自动进行垃圾回收, 这样你就不用考虑申请或释放内存空间了. 当然, 你也可以主动进行垃圾回收或禁用自动垃圾回收, 详情参考 Python 标准库 [`gc`](https://docs.python.org/zh-cn/3/library/gc.html).


Python 是这样实现这一功能的: 每个对象都有一个引用计数器, 计数器记录着当前指向该对象的引用的数目, 一旦这个计数器被设置为 0, 那么这个对象占用的内存空间就会被自动回收. 由于垃圾回收是 Python 自动完成的, 这意味着你可以在脚本中任意使用对象而不需要考虑申请或释放内存空间, 在程序运行时, Python 将会自动清理那些不再使用的空间, 与 C/C++ 相比, 这样做省去了大量的基础代码.


> 基于引用计数器实现的垃圾回收, 只适用于标准 Python (CPython), 诸如 PyPy, Jython 等其他实现方案可能会采用不同的机制, 但最后的效果都是类似的, 都会自动回收未使用的内存空间.
> 



## 二. 共享引用


### 不可变对象的共享引用


看看这个例子:


```python
>>> a = 3
>>> b = a
```


首先, 变量 `a` 引用了对象 3, 变量 `b` 引用了变量 `a`. 变量 `a` 正在使用, 因此 `a` 被替换成其引用的对象 `3`, 从而 `b` 也成为对象 `3` 的一个引用. 最终的效果就是变量 `a` 和变量 `b` 都引用了相同的对象 `3` (即指向了相同的内存空间), 如下图所示:


![image.png](https://cdn.nlark.com/yuque/0/2020/png/267146/1591510915674-0bfba183-7e44-40cc-99da-daafcdafba8b.png#align=left&display=inline&height=434&margin=%5Bobject%20Object%5D&name=image.png&originHeight=867&originWidth=1180&size=83216&status=done&style=shadow&width=590)


这种情况在 Python 中称为**共享引用(或共享对象)**, 即多个变量名引用了同一个对象. 注意, 变量 `a` 和变量 `b` 并没有彼此关联, 实际上在 Python 中不可能发生两个变量的相互关联. 真实情况就是两个变量通过引用都指向了同一个对象.


我们来验证一下, :


```python
>>> a = 3
>>> b = a
>>> id(a) == id(b) 
True  # 说明 a 和 b 指向同一块的内存空间
```


如果运行下面的语句, 变量 `b` 的值是什么:


```python
>>> a = 3
>>> b = a
>>> a = 'spam'
```


对于所有的赋值语句, 都是创建一个新对象, 并且将变量名引用新的对象, 上面语句的引用结构如下图所示:


![共享引用.gif](https://cdn.nlark.com/yuque/0/2020/gif/267146/1591511667256-9afbd3c1-5ba0-49ee-92da-5e296fd96b60.gif#align=left&display=inline&height=420&margin=%5Bobject%20Object%5D&name=%E5%85%B1%E4%BA%AB%E5%BC%95%E7%94%A8.gif&originHeight=839&originWidth=1395&size=452360&status=done&style=shadow&width=698)


我们来验证一下:


```python
>>> a = 3
>>> b = a
>>> a = 'spam'
>>> b
3
>>> id(a) == id(b)
False   # 说明 a 和 b 指向不同的内存空间
```


如果将上面的例子改为, 那么 `b` 的值是多少:


```python
>>> a = 3
>>> b = a
>>> a = a + 3
```


同样的原因, `a` 的值是 6, `b` 的值依旧是 3. `a` 的引用已经是新的对象了, 这并不会连带着改变 `b`, 因为对象 3 是整数(int)类型, 整数类型是不可变对象, 是不可能在原位置修改它.


到此为止, "**共享引用时, 对一个变量名的修改, 不会影响到其他曾经引用的变量**" 这种情况, 只发生在**不可变对象**上, 如果是可变对象, 那么情况会如何?


### 可变对象的共享引用


请看下面例子:


```python
>>> L1 = [1, 2, 3]
>>> L2 = L1
>>> L1[0] = 9
```


因为**赋值的行为是在目标和对象之间创建/修改绑定(bindings)关系**, 因此 `L2` 与 `L1` 都引用了同一个对象 `[1, 2, 3]` , 然后将 `L1` 引用的列表对象的第一个元素修改为 `9` , 请问此时 `L1` 和 `L2` 的值分别是多少?


下面揭晓答案:


```python
>>> L1 = [1, 2, 3]
>>> L2 = L1
>>> id(L1) == id(L2)
True
>>> L1[0] = 9
>>> L1
[9, 2, 3]
>>> L2
[9, 2, 3]
>>> id(L1) == id(L2)
True
```


上面过程的引用过程如下图所示:


![共享引用_可变对象.gif](https://cdn.nlark.com/yuque/0/2020/gif/267146/1591514313320-2d451bd1-700e-4459-83cc-89beb7f09c34.gif#align=left&display=inline&height=325&margin=%5Bobject%20Object%5D&name=%E5%85%B1%E4%BA%AB%E5%BC%95%E7%94%A8_%E5%8F%AF%E5%8F%98%E5%AF%B9%E8%B1%A1.gif&originHeight=650&originWidth=1395&size=150508&status=done&style=shadow&width=698)


可以看到, 对 `L1` 的修改, 会影响到 `L2` , 其过程如下:


1. 首先, `L1` 和 `L2` 都指向同一个对象
1. 由于引用的是**可变对象**, 因此能在 [`id()`](https://docs.python.org/zh-cn/3/library/functions.html?highlight=id#id) 值不变的情况下修改对象的值
1. 于是 `L1` 和 `L2` 的值都是改变后的值



为什么这里与引用的是**不可变对象**时是行为不一样?


1. 必须明确"**赋值语句的行为是在目标和对象之间建立绑定(bindings)关系**", 即赋值操作只是将变量名与对象建立引用关系;
1. 要深刻理解"**不可变对象不能被改变. 如果一个变量必须存储一个不同的值, 则必须创建新的对象**"和"**可变对象可以在其 **[**`id()`**](https://docs.python.org/zh-cn/3/library/functions.html#id)** 值保持固定的情况下改变其取值**";
1. 对变量名的操作, 实际上是对这个变量引用的对象进行操作.
1. 最后, 也是最关键的是, Python 缓存的可以进行复用的对象是**不可变对象**, 可变对象是不会做缓存的(这一点请看下面的例子);
1. 综上所述, 对一个变量这是由"引用的对象是不是可变对象"引起的, 而不是由赋值语句引起的. 



```python
>>> L1 = [1, 2, 3]
>>> L2 = [1, 2, 3]  # 创建新对象, 因为 Python 不会缓存可变对象
>>> id(L1) == id(L2)  # 所以 id 值不相同, L1 和 L2 是完全不同的对象
False
```


前面的例子中:


- `a = 3; b = a; a = a + 3` , 由于数字是不可变对象, 所以对数字的操作会**创建新的对象**, 所以后面的变量 `a` 与 `b` 的 id 值是不同的, 所以对变量 `a` 的操作不会影响到变量 `b`;
- 而如果引用的是可变对象, `L1 = [1, 2, 3]; L2 = L1; L1[0] = 9` , 由于列表是可变对象, 可变对象支持在原位置修改值,** **因此对 `L1` 的修改不会改变  [`id()`](https://docs.python.org/zh-cn/3/library/functions.html#id) 值, 而 `L1` 和 `L2` 都引用了同一个 [`id()`](https://docs.python.org/zh-cn/3/library/functions.html#id) 值, 所以最后的表现就是"修改了 `L1`, `L2` 也被修改"



所以, 给变量赋值时, 一定要注意引用的是可变对象还是不可变对象, 不注意这一点, 冥冥之中你就踩很多坑.


### 对象复制(copy)


引用可变对象时, 修改一个引用它的变量会影响另一个引用它的变量, 大部分情况下, 这是我们想要的效果.


但如果你不想要这样的现象发生, 引用可变对象时, 也想像引用不可变对象那样工作,  那怎么办?


莫慌, 号称瑞士军刀的 Python 已经帮你想好了: 使用对象复制(copy).


复制一个对象有多种操作, 有些对象自带复制(copy)方法, 自带的复制方法一般都是浅拷贝, 如果没有自带复制方法就需要借助内置的 `[copy](https://docs.python.org/zh-cn/3/library/copy.html)` 模块.


还是上面的例子, 我们复制一份 `L1` 的副本:


```python
>>> L1 = [1, 2, 3]
>>> L2 = L1[:]  # 复制一个列表有多种方法, 这里用的切片就是其中一种, 关于列表的详细使用, 请阅读后面关于列表的章节.
>>> id(L1) == id(L2)
False
>>> L1[0] = 9
>>> L1
[2, 2, 3]
>>> L2
[1, 2, 3]
>>> id(L1) == id(L2)
False
```


对象复制分为浅层复制(**shallow copy**)和深层复制(**deep copy**), 即我们通常说的**浅拷贝**和**深拷贝**.


- 浅拷贝 (**shallow copy**): 只拷贝父对象, 不会拷贝对象的内部的嵌套对象. 可以使用对象自带的方法或 [`copy.copy(x)`](https://docs.python.org/zh-cn/3/library/copy.html#copy.copy) 方法实现浅拷贝
- 深拷贝 (**deep copy**):  完全拷贝了父对象及其嵌套对象, 即复制一份完全一样的副本. 使用 [`copy.deepcopy(x[, memo])`](https://docs.python.org/zh-cn/3/library/copy.html#copy.deepcopy) 方法实现深拷贝.



> 其实浅拷贝和深拷贝, 只对可变对象有效果, 对不可变对象没必要进行对象复制.



下面给出两个例子体验一下浅拷贝和深拷贝:


```python
>>> # 浅拷贝: 只拷贝父对象, 不会拷贝对象的内部的子对象
>>> a = [1, 2, [3, 4, 5]]  # 创建一个嵌套列表
>>> b = a[:]  # 切片复制属于浅拷贝, list.copy() 方法也是浅拷贝
>>> id(a) == id(b)
False
>>> id(a[0]) == id(b[0])  # 不可变对象有缓存
True
>>> id(a[2]) == id(b[2])  # 浅拷贝不会复制嵌套对象. 如果是深拷贝这里就是 False
True
>>> a[0] = 0   # 这个不会影响 b
>>> a
[0, 2, [3, 4, 5]]
>>> b
[1, 2, [3, 4, 5]]
>>> id(a) == id(b)
False
>>> a[2][0] = 9  # 由于 a 的第三个元素还是引用, 并不是一个副本, 所以这个会影响 b
>>> a
[0, 2, [9, 4, 5]]
>>> b
[1, 2, [9, 4, 5]]
>>> id(a) == id(b)
False
```


```python
>>> # 深拷贝: 完全拷贝了父对象及其嵌套对象
>>> from copy import deepcopy  # 深拷贝需要使用内置模块 copy.deepcopy 方法
>>> a = [1, 2, [3, 4, 5]]
>>> b = deepcopy(a)
>>> id(a) == id(b)
False
>>> id(a[2]) == id(b[2])  # 深拷贝会复制嵌套对象
False
>>> a[0] = 0
>>> a
[0, 2, [3, 4, 5]]
>>> b
[1, 2, [3, 4, 5]]
>>> a[2][0] = 9  # a 无论怎么改, 都不会影响 b
>>> a
[0, 2, [9, 4, 5]]
>>> b
[1, 2, [3, 4, 5]]
```


### 缓存机制


一般而言, 垃圾回收行为会在引用计数器变为 0 时马上回收, 但对于特定的类型而言可能不完全是这样.


考虑下面代码:


```python
>>> x = 3
>>> x = 'demo'
```


因为 Python 缓存并复用了**小的整数**和**小的字符串**, 这里的对象 `3` 可能不会被回收, 它可能仍被存在一个系统表中, 等待下一次你的代码里生成另一个 `3` 来重复利用. 尽管这样, 大多数种类的对象都会在不再被引用时马上回收, 对于那些不会被回收的对象, 缓存机制并不影响你所编写的代码.


### 相等判断


基于 Python 的引用模型, 有两种方法可以检查是否相等:


- `==` 运算符: 测试两个被引用的对象是否具有相同的**值**
- `is` 运算符: 检查对象的同一性, 即精确地指向同一个对象. 实际上比较的是引用的**指针**, 也就是比较 `id()` 值



```python
>>> L = [1, 2, 3]
>>> M = L
>>> id(L)
2405635346880
>>> id(M)
2405635346880
>>> L == M
True
>>> L is M
True
>>> M is L
True
```


```python
>>> L = [1, 2, 3]
>>> M = [1, 2, 3]
>>> id(L)
2405635242368
>>> id(M)
2405635372736
>>> L == M
True
>>> L is M
False
>>> M is L
False
```


```python
>>> # 小的整数和小的字符串才被缓存
>>> x = 3
>>> y = 3
>>> id(x)
140709415147232
>>> id(y)
140709415147232
>>> x == y
True
>>> x is y
True
```


```python
>>> # 小的整数和小的字符串才被缓存
>>> x = 123456798
>>> y = 123456798
>>> id(x)
2405635145616
>>> id(y)
2405635580816
>>> x == y
True
>>> x is y
False
```


## 四. "弱"引用


关于对象的垃圾回收, 不得不面对循环引用的问题, 即一个对象有可能引用自身, 或者引用另一个自身的对象, 例如: `L.append(L)` , 由于这样的对象的引用计数器不会清零, 因此永远不会被回收.


在实际开发中, 使用弱引用在一定程度上可以避免不必要的循环引用. 因为弱引用不能保证对象存活: 当对象的引用只剩弱引用时， [garbage collection](https://docs.python.org/zh-cn/3/glossary.html#term-garbage-collection) 可以销毁引用并将其内存重用于其他内容。但是，在实际销毁对象之前，即使没有强引用，弱引用也一直能返回该对象。


简单来说, 弱引用是通过 `weakref` 标准库来实现的一种用于防止对象被垃圾回收的引用(这一引用并非来源于自身).


如果对象的最后一次引用是弱引用, 那么这个对象将被重新声明, 而相应的弱引用会被自动删除(或被告知).


弱引用的主要用途是实现保存大对象的高速缓存或映射, 但又并希望大对象仅仅因为它出现在高速缓存或映射中而保持存活.


弱引用对基于字典的大对象缓存来说十分有用, 否则, 单靠缓存的引用并不能确保对象存在与内存中, 这种情况仍然可以视为引用模型的一种特例.


并非所有对象都可以被弱引用. 可以被弱引用的对象包括类实例, 用 Python（而不是用 C）编写的函数, 实例方法, 集合, 冻结集合, 某些文件对象, 生成器, 类型对象, 套接字, 数组, 双端队列, 正则表达式模式对象以及代码对象等.


关于更多细节, 参考 `weakref` 标准库手册: [https://docs.python.org/zh-cn/3/library/weakref.html](https://docs.python.org/zh-cn/3/library/weakref.html)


## 五. 小结


在 Python 中, **变量总是一个指向对象的指针, 对变量的操作实际上是对其引用的对象的操作**.


- 如果引用的对象的**不可变对象**, 那么给变量重新赋值, 会创建新的对象, 而不会影响到其他引用源对象的变量的值;
- 如果引用的对象是**可变对象**, 那么对这个对象的修改, 会影响到所有引用这个对象的变量. 如果你想修改当前这个变量的值, 而不影响其他引用这个对象的变量的值, 此时你就需要对原对象复制(copy)一份副本, 而复制又分为浅层复制(**shallow copy**)和深层复制(**deep copy**), 即我们通常说的**浅拷贝**和**深拷贝**. 有些对象(如: 列表 list, 字典 dict)会自带复制(copy)的方法, 这些对象自带的复制(copy)方法一般都是浅拷贝, 如果需要深拷贝, 则需要使用内置库 [`copy`](https://docs.python.org/zh-cn/3/library/copy.html) 的 `copy.deepcopy` 方法.



而**赋值, 是创建引用, 并不会复制对象**.

在对象的声明周期结束后, Python 会对其进行回收, 在 CPython 实现中, 是基于引用计数模型实现的.

总之, 在 Python 中, 任何东西看起来都是通过赋值和引用工作的, 如赋值语句, 函数传参, `for` 循环遍历, 模块导入, 类属性等.


从实际的角度来说, 动态类型意味着你将写更少的代码, 同时, 动态类型也是**多态**的.










# 装饰器





## 一. 前言


1. 初次学习 Python 装饰器, 不要被"一等公民", "闭包"等概念吓到
1. 装饰器本质是一个函数或类, `@` 只是个语法糖
1. 学习装饰器, 需要有对装饰器有**还原**的能力, 即还原为函数调用或类调用的关系



## 二. 函数的特点




Python 函数具有以下 4 个特点(一等公民):


1. 函数也是对象, 可以把函数的**名字**赋值给变量
1. 函数对象(函数名字)可以当做另一个函数的参数
1. 函数可以嵌套, 即在函数里面可以定义函数
1. 函数对象可以作为函数的返回值



**说明:**


1. 上面提到的 **函数对象 = 函数名字**, 就把**函数名字**当成**变量**对待就好了
1. 变量可以赋值, 也可以作为函数参数
1. **函数的名字**(函数对象)同样可以赋值, 也可以作为函数参数



```python
>>> def func(msg):
...     return msg
... 
>>> send_message = func  # 1. 函数对象 = 函数的名字, 这里函数的名字是 func, func 可以赋值给另一个变量 send_message
>>> def call_you(func, message):  # 2. 函数对象(函数名)可以当做另一个函数的参数
...     return func(message)      
... 
>>> def call_you(message):
...     def get_message(message):  # 3. 函数可以嵌套, 即在函数里面可以定义函数
...         return message
...     return get_message  # 4. 函数对象(函数名字)可以作为函数的返回值
... 
>>>
```


**补充: 可调用**
**
我们经常使用函数, 使用函数无非就 2 点: 定义函数和使用(**调用**)函数.


我们是如何调用函数的? 在函数后面加一对圆括号 `()` 就表示调用函数. 圆括号里加点调料, 这些调料叫**参数**.


这种对象可以加圆括号调用的关系叫**可调用**(callable), 可调用对象调用时, 实际上调用的是这个对象的 `__call__` 方法. 若一个对象没有 `__call__` 方法, 则这个称这个对象**不可调用**.


> 对于类, 类名后面加圆括号, 叫**实例化对象**, 调用的是 `__init__` 方法.



假如有这么一个函数:


```python
>>> def func(*args, **kwargs):
...     print(f"args: {args}")
...     print(f"kwargs: {kwargs}")
... 
>>> func  # 函数名 = 函数对象
<function func at 0x03C5A418>
>>> func()  # 函数调用, 就在函数名后面加一对圆括号, 等价于: func.__call__()
args: ()
kwargs: {}
>>> func('a', 'b', 'c', aa='aa', bb='bb')  # 圆括号里加点参数, 等价于: func.__call__('a', 'b', 'c', aa='aa', bb='bb')
args: ('a', 'b', 'c')
kwargs: {'aa': 'aa', 'bb': 'bb'}
>>> callable(func) # 验证一下 func 是可调用对象, 等价于: '__call__' in dir(func)
True
```
**
再看一下类的情况:

```python
>>> class Kls:
...     def __init__(self, *args, **kwargs):
...         self.args = args
...         self.kwargs = kwargs
...         
>>> Kls  # 类名 = 函数对象
<class '__main__.Kls'>
>>> instance = Kls()  # 实例化, 调用 __init__ 方法
>>> instance
<__main__.Kls object at 0x0498E790>
>>> callable(instance) # 等价于: '__call__' in dir(instance)
False   # 不是可调用对象, 因为实例里没有实现 __call__ 方法
>>> instance()  # 调用可调用对象, 就报错
Traceback (most recent call last):
  File "<input>", line 1, in <module>
TypeError: 'Kls' object is not callable
>>> # 如何让类实例可调用? 实现 __call__ 方法:
>>> class Kls:
...     def __init__(self, *args, **kwargs):
...         self.args = args
...         self.kwargs = kwargs
...     
...     def __call__(self):
...         print(f"args: {self.args}")
...         print(f"kwargs: {self.kwargs}")
... 
>>> instance = Kls('a', 'b', 'c', aa='aa', bb='bb')
>>> callable(instance)
True
>>> instance()  # 调用 __call__ 方法
args: ('a', 'b', 'c')
kwargs: {'aa': 'aa', 'bb': 'bb'}
```
**
**再具体一点:**
**

1. 要调用一个函数, 就在函数名后面加圆括号 `()` 
1. 同理, 要调用一个类, 就在类名后面加圆括号 `()` 
1. 总之, **要调用某个对象, 就在这个对象后面加圆括号 `()`** 



## 三. 什么是装饰器


> 以函数装饰器为例.



函数装饰器是同时拥有上面  4  个特点的函数, 进一步地:


1. 装饰器是一个函数
1. 这个函数内部**至少**有一个嵌套函数
1. 这个函数或其内部函数, 至少有一个参数是函数对象(可调用)
1. 这个函数的返回值是函数对象(内部函数名)




装饰器就是这么贪心, 全部特点它都有.


既然装饰器是一个函数, 那么我们关注的是: 函数定义和函数使用.


**定义一个函数装饰器(函数定义):**


```python
def my_decorator(func):
	def wrapper(*args, **kwargs):
		print('Before call func')
        ret = func(*args, **kwargs)
        print('After call func')
        return ret
    return wrapper
```


**定义普通函数(方式1):**


```python
def hello():
    """ 定义一个普通函数 """
    print('Nice to meet you')

hello = my_decorator(hello)  # 调用一下 my_decorator 这个函数
```


**定义普通函数(方式2):**


```python
@my_decorator
def hello():
    """ 定义一个普通函数 """
    print('Nice to meet you')
```


上面定义普通函数的两种方式是完全等价的.


```python
>>> greet.__name__  # greet 就是 my_decorator 里面的 wrapper 对象
>>> callable(greet)  # True
>>> greet()
Before call func
Nice to meet you
After call func
```


总结一下, 使用函数装饰器的过程:


1. 定义函数装饰器: 将函数 4 大特征集成在一起
1. 使用装饰器方式:
   1. 方式1: 调用装饰器函数(my_decorator), 并传入目标函数对象(hello), 并返回同名函数(hello)
   1. 方式2: 在定义目标函数(hello)时, 在紧跟着的上面一行使用 `@<装饰器函数>` 



然而, 我们在大多数情况下都是直接看到 `@` 语法糖, 然后不知所措, 一脸懵逼. 我们需要**还原装饰器**.

### 装饰器还原



1. 看到 `@` 装饰器, 需要一双火眼金睛, 看出它的本来面目, 不管 `@` 怎么化妆, 都需要**还原为最原始的使用方式**
1. 还原思想与步骤: 
   1. 定义装饰器时, 最里面倒数第二层, 函数参数有且只有一个
   1. `@` 后面的**所有部分**(**装饰器函数**)必须是可调用的(callable)
   1. `@` 下面的函数对象作为装饰器函数的参数传入到装饰器函数里
   1. **上面修饰下面**, 即当有多个装饰器时, 装饰的顺序是上面修饰下面



**来点例子吧:**


```python
@my_decorator
def celebrate(name, message):
    pass

## 还原:
celebrate = my_decorator(celebrate)
```


```python
@repeat(4)
def greet(msg): 
    pass

## 还原:
greet = repeat(4)(greet)
```


```python
class Count:
    def __init__(self, func):
        self.func = func
        self.num_calls = 0
        print('Count __init__')

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print('num of calls is: {}'.format(self.num_calls))
        return self.func(*args, **kwargs)

@Count
def example():
    print("hello Count")
    
## 还原:
example = Count(example)  # 实例化对象
example()                 # 调用类实例对象, 由 __call__ 实现
```


```python
import functools

def my_decorator1(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('my_decorator1 - 1')
        func(*args, **kwargs)
        print('my_decorator1 - 2')
    return wrapper


def my_decorator2(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('my_decorator2 - 1')
        func(*args, **kwargs)
        print('my_decorator2 - 2')
    return wrapper

def my_decorator3(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('my_decorator3 - 1')
        func(*args, **kwargs)
        print('my_decorator3 - 2')
    return wrapper


@my_decorator1
@my_decorator2
@my_decorator3
def greet(message):
    print(message)

greet('hello world')

## 还原:
greet = my_decorator1(my_decorator2(my_decorator3(greet)))
```


## 四. 内置装饰器


常见的内置装饰器:


```python
@property
@classmethod
@staticmethod
@functools.wraps(func)
```


## 五. 装饰器的作用


1. 功能增强: 增强函数的功能, 但又不改动函数的代码
1. 状态保持: 如上面 `Count` 的例子



# 可迭代对象, 迭代器, 生成器

![](pic/1.png)