
List = [1, 0, 0, 1, 1, 0, 0, 0, 0, 1]
result = 0
for digits in List:
    result = (result << 1) | digits
print(result)


bin_num = ""
for digits in List:
   bin_num += str(digits)
print(int(bin_num, 2))