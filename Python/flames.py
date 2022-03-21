# Flames in Python

name1 =input("Enter First name")
name2 = input("Enter Second name")


def ConvertToList(string):
    list1=[]
    list1[:0]=string
    return list1
  
nameList1=ConvertToList(name1)
nameList1=ConvertToList(name2)

print(nameList1)



def remove_common(list1, list2):
 
    for i in range(len(list1)) :
        for j in range(len(list2)) :
 
            if list1[i] == list2[j] :
                c = list1[i]
 
                list1.remove(c)
                list2.remove(c)
 
                list3 = list1 + ["*"] + list2
 

                return [list3, True]