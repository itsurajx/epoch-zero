# if-elif-else statement: when you have more than two possible outcomes, use elif (short for "else if"). python checks each condition from top to bottom and runs the first one that is true. the rest are skipped entirely.

marks = 82

if marks >= 90:
    print("grade: a")
elif marks >= 75:
    print("grade: b")
elif marks >= 60:
    print("grade: c")
elif marks >= 40:
    print("grade: d")
else:
    print("grade: f")
