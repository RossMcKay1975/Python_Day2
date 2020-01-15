# def say_hello():
#     return "Hello World!"
#
# hi = say_hello
#
# print(hi())
#
# def function_caller(callback):
#     return callback()
#
# print(function_caller(hi))
#
# def outer_function():
#     def inner_function():
#         print("Hello from the inner function")
#     inner_function()
#
# outer_function()
#

def make_pretty(callback):
    def wrapper():
        print("I am a decorated function!")
        callback()
    return wrapper

@make_pretty
def ordinary():
    print ("I am an ordinary function :-(")

# pretty = make_pretty(ordinary)

ordinary()
# pretty()
