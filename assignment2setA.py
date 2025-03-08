#assignment
#Q.1
#Write a program to replace all occurrences of "a" with $ in a String.
string=(input("Enter string:"))
string=string.replace('a','$')
string=string.replace('A','$')
print("Modified string:")
print(string)

#Q.2
#Write a Python program to count the number of characters (character frequency) in a string

str="google.com"
s={}
for i in range(len(str)):
    x=str.count(str[i])
    s[str[i]]=x
print(s)

#Q.3
#Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead of the empty string.

Sample String General 12

Expected Result Ge12
msg = "General12"
a=msg[0:2]
b=msg[-2:]
c=a+b
print(c)

#Q.4
#Write a Python program to calculate the Length of a String without using a Library Function.
input_string = "shubhangi"
length = 0
for char in input_string:
    length = length + 1 
print(length)

#Q.5
# Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.

Sample String: 'ppk', 'abe'

Expected Result: 'abkppe'
str1=input("Enter the first string")
str2=input("Enter thr second string")
str1=str1.replace('c','k')
str2=str2.replace('k','c')
print(str1 + str2)


