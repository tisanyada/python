#MICHEAL IYANDA<br><br>
Facebook: miyanda2<br>
Github: miyanda2<br>
Gitlab: miyanda2<br>
Instagram: miyanda2<br>
Email: micheal@uplift.ng<br>
---
#Day 3
---
### Python Input, Output and Import
---
#### python output
```python
print('This sentence is output to the screen')
# Output: This sentence is output to the screen

a = 5

print('The value of a is', a)
# Output: The value of a is 5
```
---
The actual syntax of the print() function is
```python
from __future__ import print_function
print(*objects, sep=' ', end='\n')
```
---
Example
```python
from __future__ import print_function
print(1,2,3,4)
# Output: 1 2 3 4

print (1,2,3,4,sep='*')
# Output: 1*2*3*4

print (1,2,3,4,sep='#',end='&')
# Output: 1#2#3#4&
```
---
#### Output formatting
```python 
>>> x = 5; y = 10
>>> print('The value of x is {} and y is {}'.format(x,y))
The value of x is 5 and y is 10
```
---
#### Example of output formating usin idexing
```python
print('I love {0} and {1}'.format('bread','butter'))
# Output: I love bread and butter

print('I love {1} and {0}'.format('bread','butter'))
# Output: I love butter and bread
```
---
### Python Input
---
#### syntax of python input
```python 
input([prompt])
```
---
#### Example of python input
```python
>>> num = input('Enter a number: ')
Enter a number: 10
>>> num
'10
```
---
### Python Import
---
#### How to import modules
---
### Python Flow Control
If...else<br>
for loop<br>
while loop<br>
break and continue<br>
pass
---

![condition](https://cdn.programiz.com/sites/tutorial2program/files/python-if-else.jpg)

---

```python
if test expression:
    statement(s)
 ```
 
 ---
 ![if statement flow chart](https://cdn.programiz.com/sites/tutorial2program/files/Python_if_statement.jpg)
 ---
 ### Example: Python if Statement
 ```python
 # If the number is positive, we print an appropriate message

num = 3
if num > 0:
    print(num, "is a positive number.")
print("This is always printed.")

num = -1
if num > 0:
    print(num, "is a positive number.")
print("This is also always printed.")
```

### Python if...else Statement
---
####Syntax of if...else
```python
if test expression:
    Body of if
else:
    Body of else
```
---
#### Example of if...else
```python
# Program checks if the number is positive or negative
# And displays an appropriate message

num = 3

# Try these two variations as well. 
# num = -5
# num = 0

if num >= 0:
    print("Positive or Zero")
else:
    print("Negative number")
```
---
### Python if...elif...else
---
#### Syntax of if...elif...else
```python
if test expression:
    Body of if
elif test expression:
    Body of elif
else: 
    Body of else
```
---
![if...elif...else](https://cdn.programiz.com/sites/tutorial2program/files/Python_if_elif_else_statement.jpg)
---
#### Example of if...elif...else
```python
# In this program, 
# we check if the number is positive or
# negative or zero and 
# display an appropriate message

num = 3.4

# Try these two variations as well:
# num = 0
# num = -4.5

if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")
```
---
### Python Nested if statements
---
#### Python Nested if Example
```python
# In this program, we input a number
# check if the number is positive or
# negative or zero and display
# an appropriate message
# This time we use nested if

num = float(input("Enter a number: "))
if num >= 0:
    if num == 0:
        print("Zero")
    else:
        print("Positive number")
else:
    print("Negative number")
```
---
## Python For loop
---
![for loop](https://cdn.programiz.com/sites/tutorial2program/files/python-for-loop.jpg)
---
#### Syntax of for Loop
```python
for val in sequence:
	Body of for
```
---
![for loop](https://cdn.programiz.com/sites/tutorial2program/files/forLoop.jpg)
---
#### Example: Python for Loop
```python
# Program to find the sum of all numbers stored in a list

# List of numbers
numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]

# variable to store the sum
sum = 0

# iterate over the list
for val in numbers:
	sum = sum+val

# Output: The sum is 48
print("The sum is", sum)
```
---
### The range() function
```python
# Output: range(0, 10)
print(range(10))

# Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(10)))

# Output: [2, 3, 4, 5, 6, 7]
print(list(range(2, 8)))

# Output: [2, 5, 8, 11, 14, 17]
print(list(range(2, 20, 3)))	
```
---
## Python while Loop
---
### Syntax of while Loop in Python
```python
while test_expression:
    Body of while
```
---
#### Flowchart of while Loop

![for loop](https://cdn.programiz.com/sites/tutorial2program/files/whileLoopFlowchart.jpg)
---
#### Example: Python while Loop
```python
# Program to add natural
# numbers upto 
# sum = 1+2+3+...+n

# To take input from the user,
# n = int(input("Enter n: "))

n = 10

# initialize sum and counter
sum = 0
i = 1

while i <= n:
    sum = sum + i
    i = i+1    # update counter

# print the sum
print("The sum is", sum)
```
---
### while loop with else
---
#### Example 
```python
# Example to illustrate
# the use of else statement
# with the while loop

counter = 0

while counter < 3:
    print("Inside loop")
    counter = counter + 1
else:
    print("Inside else")
```
---
### Python break and continue
---
#### syntax of break 
```python
break
```
---
#### Flowchart of break
![break](https://cdn.programiz.com/sites/tutorial2program/files/flowchart-break-statement.jpg)
---
#### Example: Python break
```python
# Use of break statement inside loop

for val in "string":
    if val == "i":
        break
    print(val)

print("The end")
```
---
### Python continue statement
---
#### Syntax of Continue
```python
continue
```
---
#### continue flowchart
![continue](https://cdn.programiz.com/sites/tutorial2program/files/continue-statement-flowchart.jpg)
---
#### Example: Python continue
```python
# Program to show the use of continue statement inside loops

for val in "string":
    if val == "i":
        continue
    print(val)

print("The end")
```
---
### Python pass statement
---
#### Syntax of pass
```python
pass
```
---
#### Example: pass Statement
```python
# pass is just a placeholder for
# functionality to be added later.
sequence = {'p', 'a', 's', 's'}
for val in sequence:
    pass
```
---


#THE END
















 
