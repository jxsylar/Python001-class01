# 多进程 & 多线程


<!-- MarkdownTOC -->

- [概念](#概念)
    - [阻塞 & 非阻塞](#阻塞--非阻塞)
    - [同步 & 异步](#同步--异步)
    - [总结](#总结)
- [python 里的进程&线程](#python-里的进程线程)
- [作业1](#作业1)
- [参考资料](#参考资料)

<!-- /MarkdownTOC -->


<a id="概念"></a>
# 概念

> 多进程与多线程涉及到好多底层概念, 若想深入了解, 请阅读**操作系统原理**相关书籍.



<a id="阻塞--非阻塞"></a>
## 阻塞 & 非阻塞

<br />发起方发起之后, 按照**需不需要等待结果后才能做其他的事情**, 分为**阻塞**和**非阻塞**.<br />
<br />如果发起方发起之后, 需要等待结果返回后才能做其他事情, 称为**阻塞**.<br />
<br />如果发起方发起之后, 不需要等待结果返回后才能做其他事情, 称为**非阻塞**.<br />
<br />也就是说, 阻塞和非阻塞关注的是**程序在等待调用结果(如: 消息，返回值)时的状态.**<br />



<a id="同步--异步"></a>
## 同步 & 异步

<br />接收方在接收到发起方发送的消息后, 一直等到全部消息接收完后才可以做其他事情, 称为**同步.**<br />
<br />接收方在接收到发起方发送的消息后, 不需要一直等到全部消息接收完后才可以做其他事情, 称为**异步.**<br />

> 典型的异步编程模型: Node.js

<a id="总结"></a>
## 总结

- 阻塞非阻塞是描述发起方的行为，发起一个行为后，能不能立马做其他事，能就是非阻塞，不能就是阻塞
- 同步和异步是描述接收方的行为，接受到请求后，马上响应是同步，否则是异步
- 阻塞和非阻塞，同步和异步，是描述两端的行为



<a id="python-里的进程线程"></a>
# python 里的进程&线程

<br />模块: [multiprocessing](https://docs.python.org/zh-cn/3.7/library/multiprocessing.html) & [threading](https://docs.python.org/zh-cn/3.8/library/threading.html)<br />

- 进程间通信

   - 队列: [multiprocessing.Queue](https://docs.python.org/zh-cn/3.8/library/multiprocessing.html#multiprocessing.Queue)
   - 管道: [multiprocessing.Pipe](https://docs.python.org/zh-cn/3.8/library/multiprocessing.html#multiprocessing.Pipe)
   - 共享内存: [multiprocessing.Value](https://docs.python.org/zh-cn/3.8/library/multiprocessing.html#multiprocessing.Value), [multiprocessing.Array](https://docs.python.org/zh-cn/3.8/library/multiprocessing.html#multiprocessing.Array)
   - 加锁机制: [multiprocessing.Lock (acquire, release)](https://docs.python.org/zh-cn/3.8/library/multiprocessing.html#multiprocessing.Lock)


- 线程同步机制

   - 信号量: [threading.Semaphore](https://docs.python.org/zh-cn/3.8/library/threading.html#threading.Semaphore)
   - 事件: [threading.Event](https://docs.python.org/zh-cn/3.8/library/threading.html#event-objects)
   - 条件: [threading.Condition](https://docs.python.org/zh-cn/3.8/library/threading.html#condition-objects)



<a id="作业1"></a>
# 作业1

![pmap](images/pmap.gif)


<a id="参考资料"></a>
# 参考资料


- 怎样理解阻塞非阻塞与同步异步的区别: [https://www.zhihu.com/question/19732473](https://www.zhihu.com/question/19732473)
