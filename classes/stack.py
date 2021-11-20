import random

class Stack:
    def __init__(self):
        self.__stack = []
        print("Стек создан.")

    def push(self, value):
        self.__stack.append(value)

    def pop(self):
        try:
            return self.__stack.pop()
        except IndexError:
            print("Стек пуст.")

    def peak(self):
        try:
            print(self.__stack[len(self.__stack) - 1])
        except IndexError:
            print("Стек пуст.")

    def lenOfStack(self):
        return len(self.__stack)


someStack = Stack()
twoStack = Stack()
for i in range(random.randint(1, 50)):
    someStack.push(random.randint(0, 100))

someStack.peak()

for i in range(someStack.lenOfStack()):
    print(someStack.pop(), end=' ')
print()

someStack.peak()

twoStack.push(input("Введите значение: "))
twoStack.peak()
