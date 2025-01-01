def factorial(n):
  """
  This function calculates the factorial of a non-negative integer.

  Args:
    n: The non-negative integer.

  Returns:
    The factorial of n.
  """
  if n == 0:
    return 1
  else:
    return n * factorial(n-1)

# Get input from the user
num = int(input("Enter a non-negative integer: "))

# Calculate the factorial
result = factorial(num)

# Print the result
print("The factorial of", num, "is", result)
