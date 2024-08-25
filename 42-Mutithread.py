'''
author : Jaydatt Patel
MultiThread in Python 

class  threading.Thread(
    group: None = None,
    target: ((...) -> object) | None = None,
    name: str | None = None,
    args: Iterable[Any] = (),
    kwargs: Mapping[str, Any] | None = None,
    *,
    daemon: bool | None = None
)
'''

import threading


def fun1(str):
    for i in range(5):
        print(str)


def fun2(str, num):
    for i in range(5):
        print(str)


if __name__ =="__main__":
    t1 = threading.Thread(target=fun1, args=("+"),name = "function-1")
    t2 = threading.Thread(target=fun2, args=('-',123), name = "function-2")

    print("t1.name : ",t1.name)
    print("t2.name : ",t2.name)

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    
    print("Done!")
