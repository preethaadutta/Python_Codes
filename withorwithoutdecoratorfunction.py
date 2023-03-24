#advancedpython2
#without decorator:-
def display_message():
    print("Python is awesome")
def display(func):
    def inner():
        print("Executing",func.__name__,"function") #func.__name__ will print name of that function
        func()
        print("Finished execution")
    return inner
decorated_func=display(display_message)
decorated_func()
#output:Executing display_message function
#       Python is awesome
#       Finished execution
#=====================================================================================================================#
#with decorator:-
def display(func):
    def inner():
        print("Executing",func.__name__,"function") #func.__name__ will print name of that function
        func()
        print("Finished execution")
    return inner
@display #decorator
def display_message():
    print("Python is awesome")

display_message()
#output:Executing display_message function
#       Python is awesome
#       Finished execution
#line number 27 is equivalent to line number 10 & 11
#=====================================================================================================================#
def smartdivide(func):
    def inner(a,b):
        print("dividing ",a,"by",b)
        if b == 0:
            print("cannot divide by 0")
            return
        return func(a,b)
    return inner
@smartdivide
def divide(a,b):
    return (a/b)
val=divide(20,4)
print(val)
val=divide(10,0)
print(val)
#output:dividing  20 by 4
#       5.0
#       dividing  10 by 0
#       cannot divide by 0
#       None
#=====================================================================================================================#
#Decorator Chaining:- When we add more than one decorator in a function
def star(func):
    def inner(arg):
        print("*********************************************")
        func(arg)
        print("*********************************************")
    return inner
def perc(func):
    def inner(arg):
        print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
        func(arg)
        print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    return inner
@perc
@star
def printer(msg):
    print(msg)
printer("This is decorator chaining")
#output:%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#       *********************************************
#       This is decorator chaining
#       *********************************************
#       %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
'''
@perc
@star
def printer(msg):
    print(msg)
#this part is equivalent to this code-
perc(star(print(msg)))
'''
#=====================================================================================================================#
