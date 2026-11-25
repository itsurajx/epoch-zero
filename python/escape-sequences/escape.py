r"""
escape sequence: an escape sequence is a special character that starts with a backslash \. it lets you put things inside a string that are otherwise hard to type directly.
\n -> new line              -> "hello\nworld"
\t -> tab space             -> "name:\trahul"
\\ -> print backslash       -> "c:\\users\\rahul"
\" -> print double quotes   -> "he said \"hello\""
\' -> print single quotes   -> 'it\'s python'
"""

print("hello\nworld")
# hello
# world
print("hello\tworld")
# hello   world
print("a\\nirudh")
# a\nirudh
print("suraj\\\\\\")
# suraj\\\
print('my name is "suraj kumar"')  # -> else use single quotes 'suraj kumar'
# my name is "suraj kumar"
