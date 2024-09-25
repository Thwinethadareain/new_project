
def greet(fun):

    def wrapper(name):
        print("Hello")
        fun(name)
        print("Good Bye>")
    return wrapper  

@greet
def sayName(name):
    print(name)

sayName("Su Sandi Moe")    