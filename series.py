import sys

def fibonacci(n):
  """Iteratively computes the fibonacci number at input n
  """
  if type(n) is not int:
    raise TypeError('Argument must be an integer')
    # Because lucas() relies on fibonacci() input only (initially) needs to be validated here

  previous = 1
  result = 0
  counter = 1

  while counter <= n:
    result, previous = previous, result + previous
    counter += 1

  return(result)

def lucas(n):
  """Uses fibonacci() to compute the lucas number for input n
  """
  if n == 0:
    return 2
    # By definition
  if n == 1:
    return 1
    # By definition

  return(fibonacci(n - 1) + fibonacci(n + 1))
  # By an identity found on the Lucas number Wikipedia page

def sum_series(n, first = 0, second = 1):
  """Computes either a lucas or fibonacci number depending on if optional parameters of (2, 1) are passed in
     By default, computes a fibonacci number
  """
  if first == 0 and second == 1:
    return fibonacci(n)
  elif first + second == lucas(n):
    return lucas(n)
    # When given optional parameters are passed in, sum_series returns the appropriate lucas number
  elif first + second == fibonacci(n):
    return fibonacci(n)
  else:
    return "optional parameters are neither fibonacci nor lucas number inputs"

if __name__ == "__main__":
  """An unholy monstrosity that allows the user to compute fibonacci, lucas, and sum_series numbers depending on input
     Handles a variety of user errors, but with relative inefficiency. Could definitely be DRYed out, but for now, it works
  """
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
    while True: # Allows the user to manually quit, but otherwise continues prompting for input
      prompt = input()

      if prompt == 'quit':
        sys.exit()

      prompt = prompt.split('(')
      if prompt[0] == 'fibonacci':
        n = prompt[1].split(')')
        # Splitting the user input allows isolation of the number for typecasting
        try:
          print(fibonacci(n = int(n[0])), '\n')
          # There are probably better ways to do this...
        except ValueError:
          print('Input must be an integer')
          # ...that don't require the use of so many exception blocks

      elif prompt[0] == 'lucas':
        n = prompt[1].split(')')
        try:
          print(lucas(n = int(n[0])), '\n')
        except ValueError:
          print('Input must be an integer\n')
          # See above

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
          # sum_series is particularly difficult with the optional params
      else:
        print('That is not a recognized command\n')
        # Bad user!

  except KeyboardInterrupt:
      exit()
      # Allows for a clean exit when control-c is pressed
