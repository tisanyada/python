print('I love {0} and {1}'.format('bread','butter'))
# Output: I love bread and butter

print('I love {1} and {0}'.format('bread','butter'))
# Output: I love butter and bread

## #output of a few arithemetic expressions
x = 3
y = 4

print('The product of the two numbers is {} \n While the sum is {}'.format(x*y, x+y))
## using the range method
for i in range(1,11):
	for j in range(1,10):
		print("The mult is {} x {} = {}".format(i,j, j*i))
