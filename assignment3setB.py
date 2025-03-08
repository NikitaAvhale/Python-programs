#set B
#Q.1
#Write a Python program to convert a tuple to a string.
Tuple = ('H', 'e', 'l', 'l', 'o')
result = ''.join(map(str, Tuple))
print("Converted string:", result)

#Q.2
#Sort the tuple - Tuple-(2, 4, 6, 1, 4, 7.8, 2.7)
'''
Tuple = (2, 4, 6, 1, 4, 7.8, 2.7)
sorted_tuple = tuple(sorted(Tuple))
print("Sorted tuple:", sorted_tuple)
'''
#Q.3
#Write a Python program to get the 5th element from front and 5th element from last of a tuple.
'''
Tuple = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)

front = Tuple[4]
last = Tuple[-5]

print("5th element from front:", front)
print("5th element from last:", last)

'''
#Q.4
#Write a Python program to find the repeated items of a tuple.
'''
tuple(1,3,4,4,5)
if len(tuple) !=len(set(tuple)):
    print("repeated")
else :
    print('not reapeted')
    '''from collections import Counter

# Sample tuple
my_tuple = (1, 2, 3, 4, 5, 2, 3, 6, 7, 2)

# Count the occurrences of each element in the tuple
count = Counter(my_tuple)

# Print the repeated items
print("Repeated items in the tuple:")
for item, freq in count.items():
    if freq > 1:
        print(f"Item: {item}, Repeated {freq} times")
