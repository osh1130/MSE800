import math

# Addition, subtraction, multiplication, division
# Power and root calculation
# Trigonometric functions (sin, cos, tan)
# Error handling (e.g., divide by zero, invalid roots)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero is undefined.")
    return a / b

def power(a, b):
    return a ** b

def root(a, b):
    if a < 0 and b % 2 == 0:
        raise ValueError("Even root of negative number is not real.")
    return a ** (1 / b)

def sine(x):
    return math.sin(x)

def cosine(x):
    return math.cos(x)

def tangent(x):
    return math.tan(x)

