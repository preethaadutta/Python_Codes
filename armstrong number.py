#Armstrong number check
n=int(input("Enter a number:"))
sum=0
temp=n
while(temp>0):
    rem=temp%10
    sum=sum+(rem*rem*rem)
    temp=temp//10
if(sum==n):
    print(n,"is an armstrong number")
else:
    print(n,"is not an armstrong number")