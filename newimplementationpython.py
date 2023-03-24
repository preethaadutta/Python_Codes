#Taken from hackerrank

#How to print output in same line
#When output is in loop
n=int(input())
for i in range(1,n+1):
    print(i,end="") #It will print output without space between them
    #end="" is actually a string it converting the output into string and printing in a same line


#Program to print second largest element in array or list
#Method1
n1=int(input()) #Taking user input for number of elements of list
#Below line read inputs from user using map() function
a=list(map(int,input().strip().split()))[:n1]
a.sort()
a[-1]
a[-2]