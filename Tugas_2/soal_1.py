upto = int(input( ))

for i in range (1, (upto + 1)):
    if i % 3 == 0 and i % 5 == 0:
        print(f"fizzbuzz", end=" ")
    if i % 3 == 0:
        print(f"fizz", end=" ")
    if i % 5 == 0:
        print(f"buzz", end=" ")
    if i % 5 != 0 and i % 3 != 0:
        print (f"{i}", end=" ")
