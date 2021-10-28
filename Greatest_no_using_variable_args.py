print("\n!!!!! Program to find the greatest of 3 numbers using variable length argument !!!!\n")


def max_no(*num):
   result = num[0]
   for i in num:
       if i > result:
           result = i
   return result

print(max_no(0, 4, 0.3))