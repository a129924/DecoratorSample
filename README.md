# DecoratorSample

## 實作類似Flask或者是FastAPI的@Decorator實作方法
### example
```python =
decorator = MyDecorator()

@decorator.function()
def tst() -> None:
    print("tst")
```

## 實作class的decorator
實作class的decorator與function實作最大差異為class的實作會在__call__去實現
實作class的decorator有兩種傳入被掛上@decorator下function的方式
1. 透過__init__(self, func:Callable)
2. 透過__call__(self, func:Callable)

第一個方法類似於用`function實作decorator`的方式 單純的把function帶進去 而這種實作方式沒辦法傳入參數

### example
``` python =
from typing import Callable

class Decorator:
    def __init__(self, func: Callable) -> None:
        self.func = func

    def __call__(self, *args, **kwargs) -> Callable:
        # dosomething
        return self.func(*args, **kwargs)

app = Decorator()

@app
def tst(name: str, age: int) -> str:
    return f"{name} and {age}"

print(tst("name1", 1)) # name1 and 1
```

第二種方法可透過`__init__(self.param1, param2, ...)`把參數傳進去 再透過`__call__`去實現

### example
```python =
from typing import Any, Callable

class Decorator:
    def __init__(self, param1 : Any, param2: Any, ...) -> None:
        self.param1 = param1
        self.param2 = param2
        ...
    
    def __call__(self,func:Callable) -> Callable:
        
        def wrapper(self, *args, **kwargs) -> Callable:
            # dosomething
            print(self.param1)
            print(self.param2)
            ...

            return func(*args, **kwargs)
        
        return wrapper

app = Decorator("param1", "param2", ...)

@app
def tst(name: str, age: int) -> str:
    return f"{name} and {age}"

print(tst("name1", 1)) 
# '''
# param1
# param2
# name1 and 1
# '''

```

現在知道decorator回傳的必須是`Callable type`他才能去運作
如果要去實現`@decorator.function()`就要把function實作方法跟class實作方法相結合
把`__call__` 換到`decorator.function`內部

### example
```python = 
from typing import Any, Callable

class Decorator:
    def __init__(self, param1 : Any, param2: Any, ...) -> None:
        self.param1 = param1
        self.param2 = param2
        ...
    
    def add(self, param3 : Any = ...,) -> Callable:
        def decorator(func: Callable) -> Callable:
            # dosomething1
            def wrapper(*args, **kwargs)-> Callable:
                # dosomething2
                print(param3)
                return func(*args, **kwargs)
            
            return wrapper

app = Decorator("param1", "param2", ...)

@app.add("param3")
def tst(name: str, age: int) -> str:
    return f"{name} and {age}"

print(tst("name1", 1)) 
# '''
# dosomething1
# dosomething2
# param3
# name1 and 1
# '''
```
