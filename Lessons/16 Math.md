# Python Math

Python has a set of built-in math functions, including an extensive math module, that allows you to perform mathematical tasks on numbers.

## Built-in Math Functions
The ```min()``` and ```max()``` functions can be used to find the lowest or highest value in an iterable:

```python
x = min(5, 10, 25)
y = max(5, 10, 25)

print(x)
print(y)
```

The ```abs()``` function returns the absolute (positive) value of the specified number:

```python
x = abs(-7.25)

print(x)
```

The ```pow(x, y)``` function returns the value of x to the power of y (x<sup>y</sup>).

```python
x = pow(4, 3)

print(x)
```

## The Math Module
Python has also a built-in module called math, which extends the list of mathematical functions.

To use it, you must import the math module:

```python
import math
```

When you have imported the ```math``` module, you can start using methods and constants of the module.

The ```math.sqrt()``` method for example, returns the square root of a number:

```python
import math

x = math.sqrt(64)

print(x)
```

The ```math.ceil()``` method rounds a number upwards to its nearest integer, and the ```math.floor()``` method rounds a number downwards to its nearest integer, and returns the result:

```python
import math

x = math.ceil(1.4)
y = math.floor(1.4)

print(x) # returns 2
print(y) # returns 1
```

The ```math.pi``` constant, returns the value of PI (3.14...):

```python
import math

x = math.pi

print(x)
```

## Complete Math Module Reference
In the[ W3Schools Python Math Module Reference](https://www.w3schools.com/python/module_math.asp) you will find a complete reference of all methods and constants that belongs to the Math module.
