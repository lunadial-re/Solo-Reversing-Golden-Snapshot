username = input()
sum = 0
for char in username:
    sum+=ord(char)
checksum = sum %10
print(sum)
print(checksum)
