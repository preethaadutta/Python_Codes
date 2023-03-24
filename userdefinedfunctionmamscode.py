#User defined function
def greet1(name,grt):
    print(name+grt)
greet1('madhu','hi')

#User defined function
def greet(name,msg="Good morning!"):
    """
    This function greets to
    the person passed in as
    a parameter
    """
    print("Hello, " + name + msg)
greet('Paul')
greet("Bruce", "How do you do?")
greet(msg = "How do you do?",name = "Bruce")

#User defined function
def greetmulti(*names):
    """This function greets all
    the person in the names tuple."""

    # names is a tuple with arguments
    for name in names:
        print("Hello", name)
greetmulti("Monica", "Luke", "Steve", "John")
greetmulti("Monica")

print(greet.__doc__)
