'''
tup1=('physics','chemistry',1997,2000);
print("tup1[0]:",tup1[0])
'''
#Set A
#Q.1
#Reverse the following

tuple aTup (10, 20, 30, 40, 50)
aTup = (10, 20, 30, 40, 50)
reverse_tup = aTup[::-1]
print(reverse_tup)

#Q.2
#Write a Python program to create a list of tuples with the first element as the number and second element as the square of the number
numbers=range(1,10)
square_tuples=[(num,num**2)for num in numbers]
print(square_tuples) 

#Q.3
#3. Write a Python program to create a tuple with numbers and print one item.

number = (10, 20, 30, 40, 50, 60)

print(number[5]) 

#Q.4
#Write a Python program to unpack a tuple in several variables.
tuple=(1,2,3,4,5)
n1,n2,n3,n4,n5=tuple
print(n1)
print(n2)
print(n3)
print(n4)
print(n5)

#Q.5
#Write a Python program to add an item in a tuple.
Tuple1 = (10, 20, 30, 40)
Tuple2= (50, 60, 20)
add =Tuple1 + Tuple2
print(add)

#Q.6
#6. Copy element 44 and 55 from the following tuple into a new tuple

tuplet (11, 22, 33, 44, 55, 66)
tuple1 = (11, 22, 33, 44, 55, 66)
new_tuple = tuple1[3:5] 
print(new_tuple)
