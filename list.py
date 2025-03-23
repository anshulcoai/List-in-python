#Read a 5 number
'''
a=[]
for i in range(5):
    num=int(input("Enter a number :"))
    a.append(num)
print(a)
'''

#
'''
a=[]
for i in range(5):
    num=int(input("Enter a number :"))
    a.append(num)
print(a)
a[0]=700
print("Second data ",a[1])
print(a)
'''

#Write a program to read 5 numbers in list and print reverse.
'''
L=[]
for i in range(5):
    n=int(input("Enter a number :"))
    L.append(n)
for i in range(4,-1,-1):
    print(L[i], end="")
'''

# Sum of all numbers in list.
'''
L=[]
n=int(input("Enter a size :"))

for i in range(n):
    num=int(input("Enter a number"))
    L.append(num)
print(L)
s=0
for i in range(n):
    s=s+L[i]
print(s)    
'''

#Read 10 numbers from user and print them.
'''
a=[]
for i in range(10):
    n=int(input("Enter a number :"))
    a.append(n)
print(a)    
'''

# Ask user to enter the size of list and read n number and print.
'''
a=[]
n=int(input("Enter a size :"))

for i in range(n):
    num=int(input("Enter a number :"))
    a.append(num)
print(a)
'''

#Find minimum value in given list.
'''
a=[]
n=int(input("Enter a size :"))
for i in range(n):
    num=int(input("Enter a number :"))
    a.append(num)
print(a)
if a:
    mv=min(a)
    print("minimum value",mv)
'''
'''
L=[]
print("Enter 10 Number :")
for i in range(10):
    n=int(input())
    L.append(n)

m=L[0]    
for i in L:
    if m>i:
        m=i
print(m)        
'''

#Find Maximum value in the given list.
'''
a=[]
n=int(input("Enter a size :"))
for i in range(n):
    num=int(input("Enter a number :"))
    a.append(num)
print(a)
if a:
    mv=max(a)
    print("maximum value :",mv)
'''

# Print only even numbers from list
'''
L=[]
print("Enter 10 number :")

for i in range(10):
    n=int(input())
    L.append(n)
for y in L:
    if y%2==0:
        print(y)
'''

#
'''
L=["apple",102,"Vijay",7,5.6]
L2=L.copy()

print("Data in L",L)
L.clear() #Clear all data from list

print("Data in L",L)
print("Data in L2",L2)

L2.pop(3)

print("Data in L2",L2)
L2.extend(['a','b','c'])
print(L2)
'''

#
'''
L=[1,2,32,3,43,22,44,32,22,44]

size=len(L)
total=sum(L)
mi=min(L)
ma=max(L)
print(size)
print(total)
print(mi)
print(ma)
'''

#
'''
L=[10,90,18,6,2]
L.sort(reverse=True)
print(L)
L2=['aman','naman','aman']
c=L2.count('aman')
print(c)
L2.insert(2,"Vijay")
print(L2)
i=L2.index('aman')
print(i)
'''












