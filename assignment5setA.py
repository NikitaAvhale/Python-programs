#assignment 5
#setA
#Q.1
#Write a Python script to access the value of a key from a dictionary

'''
dict = {'a': 1, 'b': 2, 'c':3}
key ='c'
if key in dict:
    value=dict[key]
    print("value:",value)
else:
    print("key is not found")
'''
#Q.2
# Write a Python script to concatenate following dictionaries to create a new one.

#Sample Dictionary

#dic1 (1:10,2:20)

#dic2-(3:30,4:40}

#dic3 (5.50,6:603 Expected Result (1: 10,2: 20, 3: 30, 4: 40, 5: 50, 6: 601
'''
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
dic4={}
for d in (dic1,dic2 , dic3):dic4.update(d)
print(dic4)
'''
#Q.3
#3. Write a Python program to iterate over dictionaries using for loops.

'''
dic={'x':10,'y':20,'z':30}
for dict_key, dict_value in dic.items():
    print (dict_key,':',dict_value)
'''
#Q.4
#Write a Python program to sum all the items in a dictionary
'''
my_dict = {'data1': 100, 'data2': -54, 'data3': 247}

total_sum = sum(my_dict.values())

print("The sum of all items in the dictionary is:", total_sum)
'''
#Q.5
#Write a Python program to remove a key from a dictionary
'''
dic = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

del dic['a']

print(dic)
'''
