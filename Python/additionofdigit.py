num = int(input("Enter a num: "))

sum =0
while(num != 0):
    mod=num%10
    num=int(num/10)
    sum=sum+mod
print(sum)