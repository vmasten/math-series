def fibonacci(n):
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
