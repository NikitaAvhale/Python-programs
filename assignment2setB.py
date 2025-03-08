#set B
#Q.1
#Write a python program to check if a string is a Palindrome or Not.
string = input("Enter a string: ")
i = 0
palindrome = True
while i < len(string) // 2:
    if string[i] != string[len(string) - i - 1]:
        palindrome = False 
        break
    i += 1
if palindrome:
    print("It is a palindrome!")
else:
    print("It is not a palindrome.")
 
#Q.2
#Write a Python program to calculate the Number of Digits and Letters in a string.
string= input("Enter a string:")
digit=0
letter=0
for ch in string:
   if ch.isdigit():
      digit=digit+1
   else :
      letter=letter+1
print("Letters:", letter)
print("Digits:", digit)

#Q.3
#Write a Python program to remove the characters which have odd index values of a given string.
string1 = input("Enter a string:")
string2 = ""

for i in range(len(string1)):
    if i % 2 == 0:
        string2 += string1[i]
print("String after removing odd index characters:", string2)

#Q.4
#Write a Python program to count the occurrences of each word in a given sentence.
string = input ("Enter a string")
freq = {}
 
for char in string:
    freq.setdefault(char, 0)
    freq[char] += 1
 
print ("Occurrence of all characters in shubhangi is :\n "+ str(freq))




