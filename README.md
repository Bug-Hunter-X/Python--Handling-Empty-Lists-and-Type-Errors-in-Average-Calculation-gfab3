# Python: Handling Empty Lists and Type Errors in Average Calculation

This repository demonstrates a common error in Python:  how to handle edge cases such as empty lists and type errors when calculating an average. The `bug.py` file shows the initial flawed implementation. The improved version is in `bugSolution.py`.

**Problem:**
The `calculate_average` function does not handle empty input lists or lists containing non-numeric values gracefully, leading to either a `ZeroDivisionError` or a `TypeError`.

**Solution:**
The solution adds checks for an empty list and ensures all elements are numbers before performing the calculation.  This makes the function more robust and prevents unexpected crashes.