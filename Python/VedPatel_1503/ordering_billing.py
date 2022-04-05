menu={"pizza":145,"panipuri":45,"burger":90}
print(menu)
order={}
while(1):
  item=input("enter item: ")
  if(item=="done"):
    break
  else:
    q=int(input("enter quantity: "))
    order[item]=q
c=int(input("enter 1 to confirm 0 to change "))
if(c==1):
  total=0
  for i,j in order.items():
    for k,l in menu.items():
      if(i==k):
        total=total+j*l
else:
  pass



print(order) 
print(total)
    