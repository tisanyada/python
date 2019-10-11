def calc_factorial(x):
    """This is a recursive function to find the factorial of an integer"""
    try:
      if x == 1:
          return 1
      else:
          return (x * calc_factorial(x-1))
    except:
        print("The program threw an error")
num = 7
print("The factorial of", num, "is", calc_factorial(num))
