# -*- coding: utf-8 -*-
"""Copy_of_Lab_10_Colab_practice_and_requirements.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1WXJIGVCE1NnctiJ2zdqDTysJw4szniMl

# LAB 10 : UNIT TESTING


---

In this lab, we will learn the core concepts of Unit Testing in software development. The purpose of Unit Testing is to validate that individual units of source code, such as functions, methods, or classes, work as intended. Unit testing ensures that small, isolated components of a program behave correctly under different scenarios. Writing unit tests helps developers catch bugs early in the development cycle and maintain code reliability.

**What is a Unit ?**

A unit refers to the smallest testable part of an application. This could be a function, method, or class that performs a specific task. The goal of unit testing is to ensure that each unit works in isolation without depending on other parts of the program.

**Assertions in Unit Testing**

Assertions are conditions or boolean expressions that evaluate whether the output of a unit matches the expected result.

##**Running Tests Directly (Without unittest)**

For example:
"""

import unittest
def add(a, b):
    return a + b

# Unit test
def test_add():
    assert add(2, 3) == 5
    assert add(0, 0) == 0
    assert add(-1, 1) == 0
    print("All tests passed!")
if __name__ == "__main__":
    test_add()

"""Here, the assert statement verifies that the add function returns the correct result for various inputs. If the assertion fails, the test reports an error, helping identify issues in the code.

## **Running Tests Using unittest Framework**

Example using Python’s unittest:

Failing tests:
"""

import unittest
def add(a, b):
    return a + b

class TestMathOperations(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 4)
        self.assertEqual(add(-1, 1), 0)

if __name__ == "__main__":
    unittest.main(argv=[''], exit=False)

"""Successfull tests:"""

import unittest
def add(a, b):
    return a + b

class TestMathOperations(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)

if __name__ == "__main__":
    unittest.main(argv=[''], exit=False)

"""or use this line:"""

unittest.main(argv=[''], exit=False)

"""Here, the unittest.TestCase class provides methods like assertEqual to validate the output of the function being tested.

**Mocking in Unit Testing**

Mocking is a technique used to replace real components (like databases, APIs, or external systems) with simulated versions during testing. This allows you to test a unit in isolation without relying on external dependencies.
Example using Python’s unittest.mock:

directly:
"""

from unittest.mock import Mock

# Mocking an external API call
api_mock = Mock(return_value={"status": "success", "data": []})
response = api_mock()

assert response["status"] == "success"
print("Test passed!")

"""with unittest framework:"""

import unittest
from unittest.mock import Mock

class TestAPIMock(unittest.TestCase):
    def test_api_mock(self):
        # Mocking an external API call
        api_mock = Mock(return_value={"status": "success", "data": []})
        response = api_mock()

        # Assertions
        self.assertEqual(response["status"], "success")
        self.assertEqual(response["data"], [])

if __name__ == "__main__":
    unittest.main(argv=[''], exit=False)

"""**Example Problem:**

Write a Python function to calculate the factorial of a number and create unit tests for the function.

"""

import unittest

# Function to calculate factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Unit test class
class TestFactorialFunction(unittest.TestCase):
    def test_factorial(self):
        self.assertEqual(factorial(0), 1)  # Factorial of 0
        self.assertEqual(factorial(1), 1)  # Factorial of 1
        self.assertEqual(factorial(5), 120)  # Factorial of 5
        self.assertEqual(factorial(10), 3628800)  # Factorial of 10

if __name__ == "__main__":
    unittest.main(argv=[''], exit=False)

"""Explanation:

In this example:

The factorial function is the unit under test.
The unit tests validate that the function produces correct results for edge cases (n=0, n=1) and general cases (n=5, n=10).

# **Practice:**

1.Analyze and Debug a Unit Test

Below is a unit test written for the function divide_numbers(a, b):
"""

def divide_numbers(a, b):
    return a / b
# Unit test
def test_divide_numbers():
    assert divide_numbers(10, 2) == 5
    assert divide_numbers(5, 0) == "Undefined"  # This is expected to fail
    assert divide_numbers(0, 5) == 0
    print("passed")

test_divide_numbers()

"""Write your corrected code below:"""



"""2.Write unit tests for the following functions:"""

def subtract(a, b):
    return a - b

def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return a / b

"""
Tasks:

Test the subtract function with positive, negative, and zero values.

Test the divide function with:

Normal inputs.

Division by zero (should raise an exception)."""



"""# Requirement

## 1. Write Unit Tests from Scratch

###Function 1: multiply_numbers(a, b)

Write a function that multiplies two numbers and test for:

Two positive numbers.

Multiplication with zero.

Negative numbers.
"""

import unittest

def Multiply_numbers(x, y):
  if x == 0 or y == 0:
    return 0
  else:
    return x * y

class TestMultiply(unittest.TestCase):
    def test_multiply(self):
        self.assertEqual(Multiply_numbers(5, 7), 35)
        self.assertEqual(Multiply_numbers(0, 5), 0)
        self.assertEqual(Multiply_numbers(-1, 8), -8)

if __name__ == "__main__":
    unittest.main(argv=[''], exit=False)

"""###Function 2: reverse_list(input_list)

Write a function that reverses a given list and test for:

A normal list.

An empty list.

A single-element list.


"""

def Reverse_list(L):
  reversed_list = L[::-1]
  return reversed_list

class TestReverse(unittest.TestCase):
    def test_reverse(self):
        self.assertEqual(Reverse_list([1 , 2, 3, 4 , 5]), [5 , 4 , 3 , 2 , 1])
        self.assertEqual(Reverse_list([]), [])
        self.assertEqual(Reverse_list([1]), [1])

if __name__ == "__main__":
    unittest.main(argv=[''], exit=False)

"""##2. Extend Provided Code

Function 3: calculate_discount(price, discount_percentage)

Extend the function by:

Adding a test for valid inputs (e.g., price = 100, discount = 10%).

Testing invalid discounts (negative or greater than 100%).

Handling zero price or zero discount.


"""

def claculate_discount(price , discount_percentage):
  if 0 < discount_percentage <= 100:
    discount_amount = (discount_percentage / 100) * price
    discounted_price = price - discount_amount
    return discounted_price
  else:
    return "Invalid discount"

class TestDiscount(unittest.TestCase):
    def test_discount(self):
        self.assertEqual(claculate_discount(100, 10), 90)
        self.assertEqual(claculate_discount(0, 10), 0)
        self.assertEqual(claculate_discount(100, 110), "Invalid discount")

if __name__ == "__main__":
    unittest.main(argv=[''], exit=False)

"""##3. Encapsulate in a Class


Class: MathOperations

Implement a class MathOperations that contains:

Method 1: is_prime(n)

Check if a number is prime.

Test cases:

Prime numbers.

Non-prime numbers.

Edge cases like 0, 1, and negative numbers.

Method 2: factorial(n)

Compute the factorial of a number.

Test cases:

Positive integers.

Edge case: n = 0 (factorial is 1).

Invalid cases: negative numbers.
"""

class MathOperations:
    def is_prime(self, n):
      if n <= 1:
        return False
      for i in range(2, n):
        if n % i == 0:
          return False
        else:
          return True

    def factorial(self, n):
      if n < 0:
        return "Invalid input"
      elif n == 0 or n == 1:
        return 1
      else:
        return n * self.factorial(n - 1)

class TestMathOperations(unittest.TestCase):

  def test_is_prime(self):
    math_operations = MathOperations()
    self.assertTrue(math_operations.is_prime(7))
    self.assertFalse(math_operations.is_prime(4))
    self.assertFalse(math_operations.is_prime(0))

  def test_factorial(self):
    math_operations = MathOperations()
    self.assertEqual(math_operations.factorial(5), 120)
    self.assertEqual(math_operations.factorial(0), 1)
    self.assertEqual(math_operations.factorial(-1), "Invalid input")


if __name__ == "__main__":
    unittest.main(+)