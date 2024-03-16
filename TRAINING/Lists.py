'''create a list'''
lis=[1,2,3,4,5,6,7,8,9]

#accessing elements
print(lis[1])
print(lis[4])

#slicing
print(lis[:])
print(lis[:2])
print(lis[:-5])
print(lis[3:-1])

#loops accessing
for l in lis:
    print(lis[1],end="")
print(lis)

#apppend
lis.append(3)
print()
print(lis)

#insert
lis.insert(1,2)
print()
print(lis)

#multidimensional create and access
lis2=[[1,8,4],[5,9,5]]
print(lis)

#updating values
lis[2]='55'
print(lis)

#adding high and low elements of a list
l=[12,42,23,96,7,18,10,133]
min=l[0]
max=l[0]
minid=0
maxid=0
for i in range (len(l)):
    if min>l[i]:
        min=l[i]
        minid=i
    if max<l[i]:
        max=l[i]
        maxid=i
s=min+max
d=max-min
l[minid]=d
l[maxid]=s    

#write a program to find the second smallest negative number from the  list without sort min and max
mylist=[22,-1,42,65,1,-4,6]

'''def sec(list,min):
    for i in range(len(list)):
        if min>list[i]:
          min=list[i]
    return min
min=0
small=sec(mylist,min)
print(small)
mylist.remove(small)
print(sec(mylist,min))'''

def sec(list,min,sec_small):
    for i in range(len(list)):
        if min>list[i]:
          min=list[i]
    for i in range(len(list)):
        if list[i]>min and mylist[i]<=sec_small:
            sec_small=list[i]
    return min,sec_small
min=0
sec_small=0
small,seco=sec(mylist,min,sec_small)
print("second smallest num:",seco)

#shift all zeroes to right without changing order of remaining numbers
list=[2,0,1024,0,40,230,0]
n=len(i)
#12=[]
count=0
for i in range(n):
    if l[i] !=0:
        12+[1[i]]
    elif 1[i]==0:
        12[-i]=0
