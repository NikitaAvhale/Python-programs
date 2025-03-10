#seta que1
"""a=[1,2,3,4,5]
avg=sum(a)/len(a)
print("Average:",avg)"""

#que2
"""value=[1,2,5,4,5]
if len(value)!=len(set(value)):
     print("duplicate")
else:
     print("all unique")"""

#que3
"""a=int(input("enter the number between 1 to 50:"))
if(a <= 50):
 print("OK")
else:
 print("Out of range")"""
#que4
def fibonacci(n):
    a,b=0,1
    for _ in range(n):
        yield a
        a,b=b,a+b
print(list(fibonacci(10))) 

#setb que1
num=int(input("enter an integer:"))
for i in range(num):
     print 
