#Q.1
# Write a Python program to sort a dictionary by key.

#Sample Dictionary:

#color_dict = {'red''#FF0000', 'green' '#008000', 'black' '#000000','white':"#FFFFFF"}
'''
color_dict = {'red': '#FF0000','green': '#008000','black': '#000000','white': '#FFFFFF'}
sorted_keys=sorted(color_dict.keys())
sorted_dict ={}
for key in sorted_keys:
    sorted_dict[key]=color_dict[key]
for key, value in sorted_dict.items():
    print(key +':',value)
    '''
#Q.2
#Write a Python program to combine two dictionary adding values for common keys

Sample Dictionary:

d1-('a'100,'b':200,'c':300)

d2-('a':300,'b':200,'d':400)

Sample output: Counter(('a' 400, "b" 400, 'd' 400, 'c' 3001)

'''   
dic1={'a':100,'b':200,'c':300}
dic2={'a':300,'b':200,'d':400}
dic3=dic1.copy()
for key, value in dic2.items():
    if key in dic3:
        dic3[key]+=value
    else:
        dic3[key]=value
for key,value in dic3.items():
    print(f'{key}:{value}')

'''
#Q.3
#Write a Python script to generate and print a dictionary that contains a number (Between

#1 and n) in the form (x, x*x).

#Sample Dictionary (n=5)

#Expected Output {1 1,2:4, 3:9, 4: 16,5:25)
'''
n= int(input("enter a number:"))
d=dict()
for x in range(1,n+1):
    d[x]=x*x
print(d)
'''
#Q.4
#4. Write a Python program to create a dictionary from a string.

Sample-String: W3resource"

Expected output: ('3'" 1, 's: 1, 2, 1, 1, 1, 2,011
'''
sample_string = 'W3resource'
sample_string = sample_string.lower()
char_count = {}

for char in sample_string:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

print(char_count)
'''
#set C
#Q.1
#1. Write a Python program to create a dictionary from two lists without losing duplicate values.

#Sample lists: ['Class-V', 'Class-VI', 'Class-VII','Class-VIII'], [1. 2. 2, 31

#Expected Output: defaultdict(<class 'set'>, "Class-VII (2), 'Class-VI: (2), 'Class-VII (3), 'Class-V: {1}})
'''
from collections import defaultdict
class_list = ['class-v','class-vi','class-vii','class-viii']
id_list=[1,2,2,3]
temp= defaultdict(set)
for c, i in zip(class_list, id_list):
    temp [c].add(i)
print(temp)
'''
#Q.2
#2. Write a Python program to create a dictionary of keys x, y, and z where each key has as value a list from 11-20, 21-30, and 31-40 respectively. Access the fifth value of cach key from the dictionary.

#Expected Output:

{'x' [11, 12, 13, 14, 15, 16, 17, 18, 19],

'y [21, 22, 23, 24, 25, 26, 27, 28, 29].

'2' [31, 32, 33, 34, 35, 36, 37, 38, 39]) 15 25 35

x has value [11, 12, 13, 14, 15, 16, 17, 18, 19]

y has value [21, 22, 23, 24, 25, 26, 27, 28, 29]

z has value [31, 32, 33, 34, 35, 36, 37, 38, 39]
                  '''
dict = {
    'x': list(range(11, 21)), 
    'y': list(range(21, 31)), 
    'z': list(range(31, 41))  
}
print("Fifth value of x:", dict['x'][4])
print("Fifth value of y:", dict['y'][4])
print("Fifth value of z:", dict['z'][4])
for key, value in dict.items():
    print(f"{key} has value {value}")
'''
