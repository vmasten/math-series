import sys

def fibonacci(n):
  """
  """
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
  print('if at any time you wish to exit, type "quit" or use the keyboard shortcut control-c')

  print('\nfibonacci(n):\n')
  print('Returns the nth value in the fibonacci series\n')

  print('lucas(n):\n')
  print('Returns the nth value in the lucas number series\n')

  print('sum_series(n): or sum_series(n, x, y)\n')
  print('If called with one parameter, returns the nth value in the fibonacci series;\nif called with optional parameters 2 and 1 (comma-separated), returns the nth value in the lucas number series\n')

  print('Any other command will be ignored\n')

  try:
    while True:
      prompt = input()

      if prompt == 'quit':
        sys.exit()

      prompt = prompt.split('(')
      if prompt[0] == 'fibonacci':
        n = prompt[1].split(')')
        try:
          print(fibonacci(n = int(n[0])), '\n')
        except ValueError:
          print('Input must be an integer')

      elif prompt[0] == 'lucas':
        n = prompt[1].split(')')
        try:
          print(lucas(n = int(n[0])), '\n')
        except ValueError:
          print('Input must be an integer\n')

      elif prompt[0] == 'sum_series':
        n = prompt[1].split(')')
        try:
          if n[0][1] == ',':
            a, b, c = n[0].split(',')
          try:
            print(sum_series(int(a), int(b), int(c)))
          except ValueError:
              print('Input must be an integer(s)\n')
          except NameError:
              print('Input must be an integer(s)\n')
        except IndexError:
          print(sum_series(n = int(n[0])), '\n')

  except KeyboardInterrupt:
      exit()
