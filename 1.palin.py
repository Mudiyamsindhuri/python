num=int(input("enter a number"))
temp=num
rev=0
while num>0:
    dig=num%10
    rev=(rev*10)+dig
    num=num//10
    print("reverse of given number is",rev)
    if temp==rev:
        print("the number is palindrome")
    else:
            print("the number is not a palindrome")
            
