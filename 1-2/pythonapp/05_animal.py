from pydoc import Doc


class Animal:
    def __init__(self, name):
        self.name = name

    def move(self):
        print("move")

    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        print("bark")


class Duck(Animal):
    def speak(self):
        print("quack")


dog = Dog("doggy")
duck = Duck("ducky")

dog.move()
dog.speak()

duck.move()
duck.speak()
