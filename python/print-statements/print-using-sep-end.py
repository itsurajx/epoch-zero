# by default, print puts a space between multiple values and a newline at the end. you can change this using sep and end.

# sep: changes the separator between values
print("2024", "01", "15", sep="-")  # 2024-01-15
print("a", "b", "c", sep=" | ")      # a | b | c
print("suraj", "kumar", sep="")      # surajkumar

# end: changes what is printed at the end (default is \n)
print("hello", end=" ")
print("world")  # prints on same line: hello world

print("loading", end="...")
print("done!")
