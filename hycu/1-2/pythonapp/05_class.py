class Test:
    cn = "cn"

    def __init__(self, name):  # constructor
        self.name = name  # instance level variable

    def printName(self):  # method
        print(self.name)


t = Test("kim")
t.printName()  # kim

print(t.name)

print(Test.cn)  # class level variable
