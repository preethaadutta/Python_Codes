'''
iterator:-Iterator is an object which iterates on the iterable and returns one object at a time.
Iterator object must have two methods:-
1)__iter()__
2)__next()__
'''
num = [10,4,16]
val=num.__iter__()
val1=val.__next__()
print(val1)
val1=val.__next__()
print(val1)
#output:10
#       4
#=====================================================================================================================#
#Runtime error is called exception
#exception handling:-
num = [10,4,16]
val=iter(num)
while(True):
    try:
        val1=next(val)
        print(val1)
    except StopIteration:
        break
#output:10
#       4
#       16
#this is actually the code which is written behind for loop. This code consists of while loop with an iterator
#=====================================================================================================================#
