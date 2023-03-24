#WAP to print sum of all digits of a number:-
number=int(input("Enter a number:"))
temp=number
sum=0
#in java equivalent loop statement will be while (temp>0)
while temp>0:
    rem=temp%10
    sum=sum+rem
    temp=temp//10
print("Sum of all the digits is:",sum)

#WAP to print reverse of a number:-
number=int(input("Enter a number:"))
temp=number
reverse=0
#in java equivalent loop statement will be while (temp>0)
while temp>0:
    rem=temp%10
    reverse=reverse*10+rem
    temp=temp//10
print("Reverse of the number is:",reverse)

#WAP to print all the factors of a number(including 1 and that number itself):-
number=int(input("Enter a number:"))
print("Factors of this number are:")
#in c or java equivalent loop statement will be for(i=1;i<=number;i++)
for i in range(1,number+1,+1): #in python loop starting from 1 iterating to n, increment of each iteration 1
    if number%i==0:
        print(i)

#WAP to print GCD or HCF of two numbers:-
a=int(input("Enter a number:"))
b=int(input("Enter a number:"))
#in c or java equivalent loop statement will be for(int i=1;i<=a && i<=b;i++)
#in python loop starting from 1 iterating to a and b, increment of each iteration 1
for i in range(1,a+1 and b+1,+1):
    if a%i==0 and b%i==0: #in c or java equivalent statement will be if((a%i==0)&&(b%i==0))
        gcd=i
print("GCD or HCF of the number is:",gcd)

