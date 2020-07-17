#Printing the list
print("---LIST---")
L1=[8,5,4,9]
print("LIST",L1)

#Insert at position
print("\n Insert 10")
L1.insert(2,10)
print("insert Element",L1)

#Remove the element
print("\n Remove element 9")
L1.remove(9)
print("Remove",L1)

#append the integer
print("\n Append 90")
L1.append(90)
print("Append",L1)


#sort
print("\n ***Sorted List***")
L1.sort()
print("Sorted list: ",L1)
#print("sort",L1)

#Reverse the list
print("\n <-<-<-Reverse List<-<-<-")
L1.reverse()
print("Reverse",L1)

#ASS 1-C
print("\n ******Add,sub,product******")
n1=int(input("Enter the first no: "))
n2=int(input("Enter the second no: "))
print("n1=",n1,"\n","n2=",n2)
c=n1+n2
d=n1-n2
s=n1*n2
print("Add is:",c,"\n","Sub is :",d,"\n","Product is :",s)


#Ass1-D(1)
print("\n ///DIVISION///")
n1=int(input("Enter the 1No: "))
n2=int(input("Enter the 2No: "))
print("n1=",n1,"\n","n2=",n2)
d=n1/n2
d1=n1//n2
print("Int:",d1,"\n Float:",d)

#Ass1-D(2)
print("\n USER I/P")
list=[]
n=2
count=0
while count<=n:
    n1=int(input("enter the address: "))
    n2=int(input("enter the no: "))
    list.insert(n1,n2)
    count=count+1
    print(list)
else:
    r=int(input("\n enter the no u want to remove:"))
    list.remove(r)
    print(list)
b=2
for i in range(b):
    a=int(input("\n enter the no u want to append:"))
    list.append(a)
    print(list)
list.sort()
print("Sortes list: ",list)
p=int(input("\n Enter no address you want to pop:"))
list.pop(p)
#print("popped elemenet is present in address:",p)
print("\n List after element popped: ",list)
#print(list)
list.reverse()
print("\n Reverse list: ",list)

