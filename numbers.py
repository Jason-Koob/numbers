class num:
    begin = []
    even = []
    odd = []
    prime = []
    composite = []

print("How many values would you like to check?: ")
val = int(input())

while len(num.begin) <= val:
    num.begin.append(len(num.begin))
    
print("Numbers Checked: " + str(num.begin))

# for num in num.begin:
#     if num % 2 == 0:
#         num.even.append(str(num))