# naming rules
# -> must start with letter or underscore
# -> can contain letters, digits and underscores
# -> cannot start with a digit
# -> cannot use python keywords (if, for, while)
# -> names are case sensitive -> age != Age != AGE

# valid
student_name = "suraj kumar"
_count = 10
total_marks2 = 95

print(student_name, _count, total_marks2)

# invalid (commented out to prevent syntax errors):
# 2marks = 95       # starts with digit
# my-name = "suraj" # hyphens not allowed in identifier names
