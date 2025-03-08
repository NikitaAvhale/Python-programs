#if
"""
a=100
b=160
if b>a:
    print("b is greater than a")
   """
#if-else
"""
a=100
b=160
if b<a:
    print("b is greater then a")
else :
        print("a is greater than b")
"""
#if-else-elseif
"""
score = 95
if score >=90 :
    print("Grade: A")
elif score >= 80 :
       
            print("Grade: B")
elif score >= 70 :
                print("Greade: C")
else :
                    print("Greade:F")
  """                  
#nested if-else
"""
num = -56
if num>0:
    print("number is positive .")
    if num % 2 ==0:
      print("number is even.")
    else:
      print("number is odd.")
else:
    print("number is negative.")
    """
#loops
"""
fruits=["apple","banana","cherry"]
for fruit in fruits:
    print(fruit)
    """
#
"""
for i in range(5):
    print(i)
   
word="hello"
for char in word:
    print(char)
   
for i in range(0, 10, 2):
    print(i)
    
for i in range(3):
    for j in range(3):
     print(f"i={i},j={j}")

person = {"name":"Alice","age":25,"city":"New york"}
for key, value in person.items():
    print(f"{key}:{value}")
    

pairs = [(1,'a'),(2,'b'),(3,'c')]
for number, letter in pairs:
    print(f"{number}:{letter}")
   
unique_numbers = {1,2,3,4}
for number in unique_numbers:
    print(number)
  
for i in range(10):
    if i==5:
        break
    print(i)
    
for i in range(10):
    if i % 2==0:
        continue
    print(i)
    
for i in range(3):
    print(i)
else:
    print("loop finished")
    
squares=[x**2 for x in range(5)]
print(squares)

numbers=[1,2,3,4,8,6]
for num in numbers:
    print("even" if num % 2==0 else "odd",num)
    
fruits=["apple","banana","cherry"]
for index, fruit in enumerate(fruits):
    print(f"{index}:{fruit}")
    """
def add(a,b):
    return a+b
print(add(2, 3))

