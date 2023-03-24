#Program to print second largest or second maximum or second highest element in array or list

n=int(input()) #Taking user input for number of elements of list
#Below line read inputs from user using map() function
list1=list(map(int,input().strip().split()))[:n]
set1=set(list1) #Converting list into set
set1.remove(max(set1)) #Removing maximum element from set
print(set1) #Printing set after removing maximum element from that
#Printing maximum element of that set then so now the maximum element is nothing but second maximum element of actual list
print(max(set1))