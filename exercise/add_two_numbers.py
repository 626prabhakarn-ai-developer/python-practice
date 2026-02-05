#!/usr/bin/env python3
"""Simple program that adds two numbers from user input.

This script prompts for two numbers and prints their sum.
"""

def add(a, b):
    try:
        return float(a) + float(b)
    except ValueError:
        raise ValueError("Inputs must be numbers")


def main():
    a = input("Enter first number: ")
    b = input("Enter second number: ")
    try:
        result = add(a, b)
    except ValueError as e:
        print("Error:", e)
        return
    # Print as int if result is whole number
    if isinstance(result, float) and result.is_integer():
        print("Sum:", int(result))
    else:
        print("Sum:", result)


if __name__ == "__main__":
    main()
