"""
90 above -> a
81 - 90 -> b
71 - 80 -> c
61 - 70 -> d
60 and below -> fail
"""

marks = int(input("enter marks: "))

if marks >= 91 and marks <= 100:
    print("grade: a")
elif marks >= 81 and marks <= 90:
    print("grade: b")
elif marks >= 71 and marks <= 80:
    print("grade: c")
elif marks >= 61 and marks <= 70:
    print("grade: d")
elif marks >= 0 and marks <= 60:
    print("fail")
else:
    print("invalid marks")
