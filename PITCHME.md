
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
1. Keyword <i><u>def</i></u> marks the start of function header.
<br>
2. A function name to uniquely identify it. Function naming follows the same rules of writing identifiers in Python.
<br>
3. Parameters (arguments) through which we pass values to a function. They are optional.
<br>
---
4. A colon (:) to mark the end of function header.
<br>
5. Optional documentation string (docstring) to describe what the function does.
<br>
6. One or more valid python statements that make up the function body. Statements must have same indentation level (usually 4 spaces).
<br>
7. An optional return statement to return a value from the function.
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
For example:
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
	In Python 3.6 (latest version), there are 68 built-in functions. They are listed below alphabetically along with their brief description.
---

| Method | Description |
| --- | --- |
| Python abs() | returns absolute value of a number  |
| Python all() | returns true when all elements in iterable is true  |
| Python any() | Checks if any Element of an Iterable is True   |
| Python asci() | Returns String Containing Printable Representation   |
| Python bin() | converts integer to binary string  |
---
| Python bool() | Coverts a Value to Boolean   |
| Python bytearray() | returns array of given byte size |
| Python bytes() | returns immutable bytes object  |
| Python callable() | Checks if the Object is Callable  |
| Python chr() | Returns a Character (a string) from an Integer  |
| Python classmethod() | returns class method for given function  |
| Python compile() | Returns a Python code object   |




