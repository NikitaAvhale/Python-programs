#assignment 4
#set B
#Q.1
#Write a Python program to accept the strings which contains all vowels

Input = input("Enter a string: ").lower()

if all(vowel in Input for vowel in 'aeiou'):
    
    print("The string contains all vowels.")
else:
    print("The string does not contain all vowels.")

#Q.2
#Write a Python program to create a union of sets.

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

union_set = set1 | set2 

print("Union of the sets:", union_set)

#Q.3
#Write a Python program to create an intersection of sets.

set1={1,2,3,4,5}
set2={4,5, 6,7,8}

print(set1|set2)
print(set1 & set2)

#Q.4
# Write a Python program to find maximum and the minimum value in a set.
set = {10, 20, 30, 40, 50}

max_value = max(set)
min_value = min(set)

print("Maximum value:", max_value)
print("Minimum value:", min_value)

#Q.5
#Write a Python program to create set difference and a symmetric difference

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
diff=set()
for item in set1:
    if item not in set2:
        diff.add(item)
    print("set diff:",diff)
    symmetric_diff=set()
    for item in set1:
        if item not in set2:
            symmetric_diff.add(item)
    for item in set2:
        if item not in set1:
            symmetric_diff.add(item)
    print("symmetric difference:",symmetric_diff)

#Q.6
#Write a Python program to find the length of a set.
set = {1,2,3,4,5,6}
length=0
for item in set:
    length +=1
print("length of the set:",length)


#set C
#Q.2
#Write a Python program to create a shallow copy of sets.
original_set= {1,2,3,4,5}
shallow_copy_set = set()
for item in original_set:
    shallow_copy_set.add(item)
original_set.add(6)
print(original_set)
print(shallow_copy_set)

#Q.1
#Write a Python program to perform different set operations.
#Answers of set B

