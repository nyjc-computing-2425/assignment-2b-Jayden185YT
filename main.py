num = input('Enter a number (decimal only): ')
# type your code here
decimal = str(num)
decimal = decimal.split(".")
dp = len(decimal[1])


# do not change any code beyond this point
print('The number', num, 'has', dp, 'decimal places.')
