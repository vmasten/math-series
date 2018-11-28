from series import fibonacci, lucas, sum_series
import pytest

def test_assert_true():
  """A quick proof of life to make sure the configuration is correct
  """
  assert True is True

def test_fibonacci_base():
  initial = 0
  expected = 0
  assert fibonacci(initial) == expected

def test_fibonacci_step():
  initial = 1
  expected = 1
  assert fibonacci(initial) == expected

def test_fibonacci_step2():
  initial = 2
  expected = 1
  assert fibonacci(initial) == expected

def test_fibonacci_step3():
  initial = 3
  expected = 2
  assert fibonacci(initial) == expected

def test_fibonacci_step4():
  initial = 4
  expected = 3
  assert fibonacci(initial) == expected

def test_fibonacci_step5():
  initial = 4
  expected = 3
  assert fibonacci(initial) == expected

def test_fibonacci_step6():
  initial = 5
  expected = 5
  assert fibonacci(initial) == expected

def test_fibonacci_step7():
  initial = 6
  expected = 8
  assert fibonacci(initial) == expected

def test_fibonacci_step8():
  initial = 7
  expected = 13
  assert fibonacci(initial) == expected

def test_lucas0():
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
  initial = 7
  expected = 13
  assert sum_series(initial) == expected

def test_sum_series_lucas():
  initial = 7
  first = 2
  second = 1
  expected = 29
  assert sum_series(initial, first, second) == expected

def test_fibonacci_input_validation():
  actual = 3.5
  with pytest.raises(TypeError):
    fibonacci(actual)

def test_lucas_input_validation():
  actual = 1.5
  with pytest.raises(TypeError):
    lucas(actual)

def test_fibonacci_string_input():
  actual = 'jerks'
  with pytest.raises(TypeError):
    fibonacci(actual)
