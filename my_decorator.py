class MyDecorator:
    def __init__(self, path: str = r"./example") -> None:
        self.path = path

    def __call__(self, func):
        print("start")

        def wrapper(*args, **kwargs):
            print()
            return func(*args, **kwargs)

        print("end")

        return wrapper

    def add(self):
        # print(dir(self.__call__))

        def decorator(func):
            print(f"我是function :{func}")
            print(f"{self.path}")

            def wrapper(*args, **kwargs):
                print("inside wrapper")
                print(func.__name__)
                result = func(*args, **kwargs)
                self.__record_result(result)
                return result

            return wrapper

        print("inside decorator")

        return decorator

    def __record_result(self, context: str) -> None:
        import os

        if not os.path.exists(self.path):
            os.mkdir(self.path)
        with open(
            os.path.join(self.path, "log.txt"), mode="w+", encoding="UTF-8"
        ) as fw:
            fw.writelines(context)


app = MyDecorator()


@app.add()
def tst(name: str, age: int) -> str:
    return f"my name is {name} , and {age} year old"


print(tst("abc", 20))  # my name is abc , and 20 year old
