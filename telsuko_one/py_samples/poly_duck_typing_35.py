class Laptop:

    def code(self,ide):
        print(ide.execute())


class PyCharm:

    def execute(self):
        print('PyCharm: compiling....')
        print('PyCharm: Running')


class MyEditor:

    def execute(self):
        print('MyEditor: compiling....')
        print('MyEditor: Running')


if __name__ =='__main__':
    l = Laptop()
    obj = PyCharm()
    #obj = MyEditor()
    l.code(obj)
