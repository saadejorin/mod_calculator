import string

# 202 137 390 235 114 369 198 110 350 396 390 383 225 258 38 291 75 324 401 142 288 397

# Take each number mod 37 and map it to the following character set:

# ABCDEFGHIJKLMNOPQRSTUVWXYZ
# 0123456789
# _



# 1-26 is the alphabet (lowercase),
# 27-36 are the decimal digits,
# and 37 is an underscore.
List = [28, 14, 22, 30, 18, 32, 30, 12, 25, 37, 8, 4, 37, 3, 33, 35, 27, 2, 4, 3, 28]

N = ""

for items in List:
    if items in range(0,27):
       N += (string.ascii_lowercase[items])
    if items in range(27,37):
       N +=(string.digits[items-27])
    if items == 37:
       N +=("_")

print('picoCTF{'+N+"}")



