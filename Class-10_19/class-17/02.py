from time import sleep


def hello():
    sleep(5)
    print("hello")


def hi():
    sleep(1)
    print("Hi")


# Synchronous Progamming
hello()
hi()
hello()
