# you do it manually.
num_str = "42"
num_int = int(num_str)    # "42" -> 42
num_flt = float(num_str)  # "42" -> 42.0
back_to_str = str(100)    # 100 -> "100"

a = 500.1
print(int(a))  # 500 -> int() truncates decimal values towards zero

print(type(num_str), num_str)
print(type(num_int), num_int)
print(type(num_flt), num_flt)
print(type(back_to_str), back_to_str)
