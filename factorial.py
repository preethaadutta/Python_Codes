#Calculate a factorial
number=int(input("Enter a number:"))
factorial=1
#in c or java equivalent loop statement will be for(i=1;i<=number;i++)
for i in range(1,number+1,+1): #in python loop starting from 1 iterating to n, increment of each iteration 1
    factorial=factorial*i
print("Factorial:",factorial)


'''
n=int(input("Enter a number:"))
temp=n
string1=''

while temp>0:
    rem=temp%2
    #rem1=str(rem)
    string1=str(rem)+string1
    temp=temp//2
print (string1)
#print ('Hello World')
count=0
for i in range(0,len(string1)):
    if string1[i]==1:
        count=count+1
print (count)

'''