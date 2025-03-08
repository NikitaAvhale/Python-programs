#assignment 4
#set A
#Q.1
#What is the output of following program:

#sets (1, 2, 3, 4, 4) print(sets)

'''
sets={1,2,3,4,4}
print (sets)
'''
#Q.2
#Write a python program to remove and return an arbitrary set element. Raise KeyErrorif the set is empty

'''
set={1,2,3,4,5}
if len(set)==0:
    raise KeyError("the set is empty")
else:
    for item in set:
        removed_element = item
        set.remove(item)
        break
    print(removed_element)
    print(set)
    '''
#Q.3
#Write a Python program to do iteration over sets
'''
set={10,20,30,40,50}
for item in set:
    print(item)
'''
#Q.4
#Write a Python program to find maximum and the minimum value in a set.

set={10,20,30,40}
set.add(50)
print(set)
set.remove(30)
print(set)

