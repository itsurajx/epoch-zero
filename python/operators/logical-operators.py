"""
logical operators: logical operators are used to combine multiple conditions together.
and (both conditions must be true)    :     true and true = true; false and true = false (if first condition fails, second will not be evaluated).
or  (at least one condition must be true): true or true = true; true and false = true (if first condition is true, second will not be evaluated).
not (opposite)                        :     not(true and true) -> false; not(false or true) -> false; not(false and true) -> true.
"""

chemistry = 45
physics = 34

# print true if pass in both subjects: and
print(chemistry > 33 and physics > 33)  # check both conditions.

# print true if pass in any subject: or
print(chemistry > 33 or physics > 33)   # check either condition.

# invert condition: not
print(not (chemistry > 33 and physics > 33))  # inverts the boolean result.
