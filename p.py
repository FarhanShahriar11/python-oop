# # #!/bin/python3

# # import math
# # import os
# # import random
# # import re
# # import sys



# # if __name__ == '__main__':
# #     n = int(input().strip())
# # if n % 2 != 0:
# #     print("Weird")
# # elif n % 2 == 0 and 2 <= n <= 5:
# #     print("Not Weird")
# # elif n % 2 == 0 and 6 <= n <= 20:
# #     print("Weird")
# # elif n % 2 == 0 and n > 20:
# #     print("Not Weird")
# if __name__ == '__main__':
#     a = int(input())
#     b = int(input())
#     x=a+b
#     y=a-b
#     z=a*b
#     print(x,y,z)

# Read an integer from input
n = int(input("Enter an integer: "))

# Loop through all non-negative integers less than n
for i in range(n):
    print(i**2)
