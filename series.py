def fibonacci(n):
  if type(n) is not int:
    raise TypeError('Argument must be an integer')
    # Because lucas() relies on fibonacci() input only needs to be validated here
  previous = 1
  result = 0
  counter = 1

  while counter <= n:
    result, previous = previous, result + previous
    counter += 1

  return(result)

def lucas(n):
  if n == 0:
    return 2
    # By definition
  if n == 1:
    return 1
    # By definition

  return(fibonacci(n - 1) + fibonacci(n + 1))
  # By an identity found on the Lucas number Wikipedia page

def sum_series(n, first = 0, second = 1):
  if first == 2 and second == 1:
    return lucas(n)
    # When given optional parameters are passed in, sum_series returns the appropriate lucas number

  return fibonacci(n)
  # Without the optional params, sum_series returns the appropriate fibonacci number

if __name__ == "__main__":
  print('This module defines functions that implement mathematical series')
  print('...')
  print('\n fibonacci(n):\n')
  print('Returns the nth value in the fibonacci series\n')
  while True:
    prompt = input().split('(')
    n = prompt[1].split(')')
    print(int(n[0]))

