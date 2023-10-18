class Parent:
    def __init__(self, name):
        self.name = name

    def printName(self):
        print(self.name)


class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)  # 부모 클래스의 생성자 호출
        self.age = age

    def printAge(self):
        print(self.age)


c = Child("kim", 20)
c.printName()  # 부모 클래스의 메소드 사용이 가능
c.printAge()
print(c.name)
print(c.age)
