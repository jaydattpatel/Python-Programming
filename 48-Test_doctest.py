"""
author : Jaydatt Patel

doctest : 
The doctest module searches for pieces of text that look like interactive Python sessions, and then executes those sessions to verify that they work exactly as shown. There are several common ways to use doctest:
- To check that a module’s docstrings are up-to-date by verifying that all interactive examples still work as documented.
- To perform regression testing by verifying that interactive examples from a test file or a test object work as expected.
- To write tutorial documentation for a package, liberally illustrated with input-output examples. Depending on whether the examples or the expository text are emphasized, this has the flavor of “literate testing” or “executable documentation”.

"""

def factorial(n):

    import math
    if not n >= 0:
        raise ValueError("n must be >= 0") # factorial(-1) ->  ValueError: n must be >= 0
    if math.floor(n) != n:
        raise ValueError("n must be exact integer") # factorial(30.1) ->  ValueError: n must be exact integer
    if n+1 == n:  # catch a value like 1e300
        raise OverflowError("n too large") # factorial(1e100) -> OverflowError: n too large
    result = 1
    factor = 2
    while factor <= n:
        result *= factor
        factor += 1
    return result

print(factorial(10))
print(factorial(5.0))
#print(factorial(1.5))   # ValueError: n must be exact integer
#print(factorial(-1))   # ValueError: n must be >= 0


if __name__ == "__main__":
    import doctest
    doctest.testmod()