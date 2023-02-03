divisible_by_seven = []
for i in range(2000, 3201):
    if (i % 7 == 0) and (i % 5 != 0):
        divisible_by_seven.append(str(i))
print(','.join(divisible_by_seven))
