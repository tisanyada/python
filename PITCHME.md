
# Python Function
---

<h4><span style="color:black">Function Arguments</span></strong></h4>
<h4><span style="color:black">Python Recursion</span></strong></h4>
<h4><span style="color:black">Anonymous Functions</span></strong></h4>
<h4><span style="color:black">Python Modules</span></strong></h4>
<h4><span style="color:black">Python packages</span></strong></h4>

---
## Functions
<br>
<p>In Python, function is a group of related statements that perform a specific task.
Functions help break our program into smaller and modular chunks. As our program grows larger and larger, functions make it more organized and manageable.
Furthermore, it avoids repetition and makes code reusable.
<br>

---

 ###Syntax of Function
```python
def function_name(parameters):
	"""docstring"""
	statement(s)
```
---
###Above shown is a function definition which consists of following components.
- Keyword <i><u>def</i></u> marks the start of function header.
<br>
- A function name to uniquely identify it. Function naming follows the same rules of writing identifiers in Python.
<br>
- Parameters (arguments) through which we pass values to a function. They are optional.
<br>
---
- A colon (:) to mark the end of function header.
<br>
- Optional documentation string (docstring) to describe what the function does.
<br>
- One or more valid python statements that make up the function body. Statements must have same indentation level (usually 4 spaces).
<br>
- An optional return statement to return a value from the function.
---

### Example of Function.
<br>
```python
def greet(name):
"""this function greets the person passed in as parameter"""
print("hello, " +  name + ". Good morning")
```
---

###Function Call.

Once we have defined a function, we can call it from another function, program or even the Python prompt. To call a function we simply type the function name with appropriate parameters.
---

###Docstring

The first string after the function header is called the docstring and is short for documentation string. It is used to explain in brief, what a function does.
Although optional, documentation is a good programming practice. Unless you can remember what you had for dinner last week, always document your code.
In the previous example, we have a docstring immediately below the function header. We generally use triple quotes so that docstring can extend up to multiple lines. This string is available to us as __doc__ attribute of the function.
---
###For example:
```python
print(greet.__doc__)
This function greets to
	the person passed into the name parameter.
```
---
###Scope and Lifetime of variables
Scope of a variable is the portion of a program where the variable is recognized. Parameters and variables defined inside a function is not visible from outside. Hence, they have a local scope.

Lifetime of a variable is the period throughout which the variable exits in the memory. The lifetime of variables inside a function is as long as the function executes.
---
They are destroyed once we return from the function. Hence, a function does not remember the value of a variable from its previous calls.
Here is an example to illustrate the scope of a variable inside a function.

```python
def my_func():
    x = 10
    print ("value inside function:",x)
x = 20
my_fun()
print ("value outside function:",x)
```
---
###Types of Functions

Basically, we can divide functions into the following two types:

   1. Built-in functions - Functions that are built into Python.
   2. User-defined functions - Functions defined by the users themselves.

---
###Built-in functions

   The Python interpreter has a number of functions that are always available for use. These functions are called built-in functions.
    Functions like print(), input(), range() etc. that we have been using, are some examples of the built-in functions.
	In Python 3.6 (latest version), there are about 68 built-in functions. They are listed below alphabetically along with their brief description.
---

| Method | Description |
| --- | --- |
| Python abs() | returns absolute value of a number  |
| Python all() | returns true when all elements in iterable is true  |
| Python any() | Checks if any Element of an Iterable is True   |
| Python asci() | Returns String Containing Printable Representation   |
| Python bin() | converts integer to binary string  |
---
| Method | Description |
| --- | --- |
| Python bool() | Coverts a Value to Boolean   |
| Python bytearray() | returns array of given byte size |
| Python bytes() | returns immutable bytes object  |
| Python callable() | Checks if the Object is Callable  |
| Python chr() | Returns a Character (a string) from an Integer  |
| Python classmethod() | returns class method for given function  |
| Python compile() | Returns a Python code object   |

###user-defined functions
Functions that we define ourselves to do certain specific task are referred as user-defined functions. The way in which we define and call functions in Python are already discussed.
Functions that readily come with Python are called built-in functions. If we use functions written by others in the form of library, it can be termed as library functions.
All the other functions that we write on our own fall under user-defined functions. So, our user-defined function could be a library function to someone else.
---
###Advantages of user-defined functions
User-defined functions help to decompose a large program into small segments which makes program easy to understand, maintain and debug.
If repeated code occurs in a program. Function can be used to include those codes and execute when needed by calling that function.
Programmars working on large project can divide the workload by making different functions.
---
###Example of a user-defined function
```python
# Program to illustrate
# the use of user-defined functions

def add_numbers(x,y):
   sum = x + y
   return sum

num1 = 5
num2 = 6

print("The sum is", add_numbers(num1, num2))
```
---
##Python Recursion.
Recursion is the process of defining something in terms of itself.
A physical world example would be to place two parallel mirrors facing each other. Any object in between them would be reflected recursively.
---
###Python Recursive Function
We know that in Python, a function can call other functions. It is even possible for the function to call itself. These type of construct are termed as recursive functions.
Following is an example of recursive function to find the factorial of an integer.
Factorial of a number is the product of all the integers from 1 to that number. For example, the factorial of 6 (denoted as 6!) is 1*2*3*4*5*6 = 720.
---
###Example of recursive function
```python
# An example of a recursive function to
# find the factorial of a number

def calc_factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""

    if x == 1:
        return 1
    else:
        return (x * calc_factorial(x-1))

num = 4
print("The factorial of", num, "is", calc_factorial(num))
```
---
In the above example, calc_factorial() is a recursive functions as it calls itself.

When we call this function with a positive integer, it will recursively call itself by decreasing the number.

Each function call multiples the number with the factorial of number 1 until the number is equal to one. This recursive call can be explained in the following steps.

calc_factorial(4)              # 1st call with 4
4 * calc_factorial(3)          # 2nd call with 3
4 * 3 * calc_factorial(2)      # 3rd call with 2
4 * 3 * 2 * calc_factorial(1)  # 4th call with 1
4 * 3 * 2 * 1                  # return from 4th call as number=1
4 * 3 * 2                      # return from 3rd call
4 * 6                          # return from 2nd call
24                             # return from 1st call
Our recursion ends when the number reduces to 1. This is called the base condition.
Every recursive function must have a base condition that stops the recursion or else the function calls itself infinitely.
---
###Advantages of recursion
Recursive functions make the code look clean and elegant.
A complex task can be broken down into simpler sub-problems using recursion.
Sequence generation is easier with recursion than using some nested iteration.
---
###Disadvantages of recursion
Sometimes the logic behind recursion is hard to follow through.
Recursive calls are expensive (inefficient) as they take up a lot of memory and time.
Recursive functions are hard to debug.
---
###Assignments
Design a Python Program to Display Fibonacci Sequence Using Recursion
Design a Python Program to Find Factors of Number
Design a Python Program to Count the Number of Each Vowel
---
#Python Modules
---
###Python Modules
Modules refer to a file containing Python statements and definitions.
A file containing Python code, for e.g.: <i>example.py</i>, is called a module and its module name would be <i>example</i>.
We use modules to break down large programs into small manageable and organized files. Furthermore, modules provide reusability of code.
We can define our most used functions in a module and import it, instead of copying their definitions into different programs.
Let us create a module. Type the following and save it as <i>example.py</i>.
---

### Python Module example
```python
def add(a, b):
   """This program adds two
   numbers and return the result"""

   result = a + b
   return result
```
Here, we have defined a function add() inside a module named example. The function takes in two numbers and returns their sum.
---
We can import the definitions inside a module to another module or the interactive interpreter in Python.
We use the <i>import</i> keyword to do this. To import our previously defined module example we type the following in the Python prompt.
---
```python
>>> import example
```
---
This does not enter the names of the functions defined in example directly in the current symbol table. It only enters the module name example there.
Using the module name we can access the function using dot (.) operation. For example:
```python
>>> example.add(4,5.5)
9.5
```
---
###Python import statement
We can <i>import</i> a module using import statement and access the definitions inside it using the dot operator as described above. Here is an example.
```python
# import statement example
# to import standard module math

import math
print("The value of pi is", math.pi)
```
---
###Import with renaming
We can import a module by renaming it as follows.
```python
# import module by renaming it

import math as m
print("The value of pi is", m.pi)
```
---
We have renamed the math module as m. This can save us typing time in some cases.
Note that the name math is not recognized in our scope. Hence, math.pi is invalid, m.pi is the correct implementation.

###Python from...import statement
We can import specific names form a module without importing the module as a whole. Here is an example.
```python
# import only pi from math module

from math import pi
print("The value of pi is", pi)
```
---
###Import all names
We can import all names(definitions) form a module using the following construct.
```python
# import all names form
# the standard module math

from math import *
print("The value of pi is", pi)
```
---
##Python Package
![G22222](https://cdn.programiz.com/sites/tutorial2program/files/PackageModuleStructure.jpg)

###Importing module from a package
We can import modules from packages using the dot (.) operator.
For example, if want to import the start module in the above example, it is done as follows.

```python
import Game.Level.start
```
Now if this module contains a function named select_difficulty(), we must use the full name to reference it.

Game.Level.start.select_difficulty(2)
If this construct seems lengthy, we can import the module without the package prefix as follows.
```python
from Game.Level import start
```
We can now call the function simply as follows.

```python
start.select_difficulty(2)
```
Yet another way of importing just the required function (or class or variable) form a module within a package would be as follows.

```python
from Game.Level.start import select_difficulty
```
Now we can directly call this function.

```python
select_difficulty(2)
```
Although easier, this method is not recommended. Using the full namespace avoids confusion and prevents two same identifier names from colliding.
While importing packages, Python looks in the list of directories defined in sys.path, similar as for module search path.

##Exercise.
Python Program to Display Calendar
Python Program to Shuffle Deck of Cards



