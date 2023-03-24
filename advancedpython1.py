def multiplication(x):
    print(x*2)
def calculation(func,x): #we're sending function func as an argument
    func(x)
calculation(multiplication,3) #we're sending function multiplication as an argument
#we're returning multiplication function as an argument
#output:6
#=====================================================================================================================#
#Nested function: Function within another function
def display(message): #display is outer function
    greet="I'm outer function"
    def display_message(): #display_message is inner function
        print(greet+message)
    return display_message #we're returning function as an argument
func=display("I'm inner function") #stored in func function
#execution of display_message function is over
func() #calling func function
#output:I'm outer functionI'm inner function
#=====================================================================================================================#
def display(message): #display is outer function
    print("Calling from outer function")
    def inner(): #inner is inner function
        print("Calling from inner function")
        print(message)
    inner() #calling inner() function
display("Python is awesome")
#output:Calling from outer function
#       Calling from inner function
#       Python is awesome
#=====================================================================================================================#
def display(message): #display is outer function
    print("Calling from outer function")
    def inner(): #inner is inner function
        print("Calling from inner function")
        print(message)
display("Python is awesome")
#output:Calling from outer function
#=====================================================================================================================#
