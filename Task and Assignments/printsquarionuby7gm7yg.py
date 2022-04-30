x=8
x>>=1
print(x)
x += (x%2)
print(x) 
y= x>>1
print(y)
data = []
for i in range(x):
    data.append(i*" "+"***"+" "*(x-i-1)*2+"***")
    print(data)
data.extend(data[-2::-1])
print("\n".join(data))