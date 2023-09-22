class num:
    begin = []
    even = []
    odd = []
    prime = []
    composite = []

print("How many values would you like to check?: ")
val = int(input())

# GET ALL NUMS
while len(num.begin) < val:
    num.begin.append(len(num.begin))

    # EVENS
    if len(num.begin)% 2 == 0:
        num.even.append(len(num.begin))

    # ODDS
    else:
        num.odd.append(len(num.begin))

    # PRIME
    if len(num.begin):
        num.prime.append(len(num.begin))

    # COMPOSITE
    else:
        num.composite.append(len(num.begin))
    
print("Even Numbers:          " + str(num.even))
print("Odd Numbers:           " + str(num.odd))
print("Prime Numbers:         " + str(num.prime))
print("Composite Numbers:     " + str(num.composite))