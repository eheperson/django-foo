import datetime
import time

print("")
print("-------------------------- example 1")
print("")

def foo():
    print("enivicivokki\n")

def fuu(f):
    f()

print("function foo : ",foo)
print("function fuu : ",fuu)
fuu(foo)

print("")
print("-------------------------- example 2")
print("")

def f1(func):
    def wrapper():
        print("")
        print("Is this the end of the beginning?")
        func()
        print("Or the beginning of the end?")
        print("")
    return wrapper

def f():
    print("ehe")

print(f1(f))

f1(f)() ## what the fuck is that logic?

#or 
f2 = f1(f) ## decorator is something like this line
f2()

@f1 ## f2 = f1(f) : same
def f3():
    print("enivicivokki")

f3()

print("")
print("-------------------------- example 3")
print("")


def foo3(func):
    def wrapper(*args, **kwargs):
        print("")
        print("Is this the end of the beginning?")
        func(*args, **kwargs)
        print("Or the beginning of the end?")
        print("")
    return wrapper

@foo3
def fi(a):
    print(a)

fi("yarramın başı")

@foo3
def fi2(a, b=9):
    print(a,b)

fi2("anan")

print("")
print("-------------------------- example 4")
print("")

def foo3Add(func):
    def wrapper(*args, **kwargs):
        print("")
        print("Is this the end of the beginning?")
        val =func(*args, **kwargs)
        print("Or the beginning of the end?")
        print("")
        return val
    return wrapper

@foo3Add
def add(x, y):
    return x+y

print("result of add function : ", add(12,13))
print("")

print("")
print("-------------------------- example 5")
print("")

def before_after(func):
    def wrapper(*args):
        print("before")
        func(*args)
        print("after")

    return wrapper

class Test:
    @before_after
    def decorated_method(self):
        print("run mf")

t = Test()
t.decorated_method()

print("")
print("-------------------------- example 6")
print("")

def timer(func):
    def wrapper():
        before = time.time()
        func()
        print("Function took : ", time.time() - before, "seconds")

    return wrapper

@timer
def run():
    print("ellloooo govnor")
    time.sleep(2)

run()


print("")
print("-------------------------- example 7")
print("")


def log(func):
    def wrapper(*args, **kwargs):
        with open("logs.txt", "a") as f:
            f.write("Called function with " + " ".join([str(arg) for arg in args]) + " at " + str(datetime.datetime.now()) + "\n")
        val = func(*args, **kwargs)
        return val
    return wrapper

@log
def run(a, b, c=9):
    print(a+b+c)

run(1,3, c=9)