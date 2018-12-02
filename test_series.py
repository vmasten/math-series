from series import fibonacci, lucas, sum_series
import pytest

def test_assert_true():
  """A quick proof of life to make sure the configuration is correct
  """
  assert True is True

def test_fibonacci0():
  """The sequence of test_fibonaccis test all values given in the lab spec. That seemed like enough.
  """
  initial = 0
  expected = 0
  assert fibonacci(initial) == expected

def test_fibonacci1():
  initial = 1
  expected = 1
  assert fibonacci(initial) == expected

def test_fibonacci2():
  initial = 2
  expected = 1
  assert fibonacci(initial) == expected

def test_fibonacci3():
  initial = 3
  expected = 2
  assert fibonacci(initial) == expected

def test_fibonacci4():
  initial = 4
  expected = 3
  assert fibonacci(initial) == expected

def test_fibonacci5():
  initial = 4
  expected = 3
  assert fibonacci(initial) == expected

def test_fibonacci6():
  initial = 5
  expected = 5
  assert fibonacci(initial) == expected

def test_fibonacci7():
  initial = 6
  expected = 8
  assert fibonacci(initial) == expected

def test_fibonacci8():
  initial = 7
  expected = 13
  assert fibonacci(initial) == expected

def test_lucas0():
  """Similarly, the sequence of test_lucases test all values provided in the lab spec
  """
  initial = 0
  expected = 2
  assert lucas(initial) == expected

def test_lucas1():
  initial = 1
  expected = 1
  assert lucas(initial) == expected

def test_lucas2():
  initial = 2
  expected = 3
  assert lucas(initial) == expected

def test_lucas3():
  initial = 3
  expected = 4
  assert lucas(initial) == expected


def test_lucas4():
  initial = 4
  expected = 7
  assert lucas(initial) == expected

def test_lucas5():
  initial = 5
  expected = 11
  assert lucas(initial) == expected

def test_lucas6():
  initial = 6
  expected = 18
  assert lucas(initial) == expected

def test_lucas7():
  initial = 7
  expected = 29
  assert lucas(initial) == expected

def test_sum_series_fibonacci():
  """First, sum_series is tested with an expected fibonacci() output
  """
  initial = 7
  expected = 13
  assert sum_series(initial) == expected

def test_sum_series_lucas():
  """Then, sum_series is tested with an expected lucas() output
  """
  initial = 7
  first = 11
  second = 18
  expected = 29
  assert sum_series(initial, first, second) == expected

def test_fibonacci_input_validation():
  """A test to ensure non-integers don't break fibonacci()
  """
  actual = 3.5
  with pytest.raises(TypeError):
    fibonacci(actual)

def test_lucas_input_validation():
  """And a test to ensure non-integers don't break lucas()
  """
  actual = 1.5
  with pytest.raises(TypeError):
    lucas(actual)

def test_fibonacci_string_input():
  """And finally, a test to see what happens if a string is fed to fibonacci()...
  """
  actual = 'jerks'
  with pytest.raises(TypeError):
    fibonacci(actual)

def test_lucas_string_input():
  """...and another to see what happens if a string is fed to lucas()
  """
  actual = 'jerks'
  with pytest.raises(TypeError):
    lucas(actual)
