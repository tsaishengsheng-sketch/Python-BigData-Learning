import random

lotto = []
lotto.append(random.randint(1,49))

for m in range(1,6):
    n = 0
    while n < m :
        temp = random.randint(1, 49)
        if(temp ==lotto[n]):
            n = 0
        else:
            n += 1
    lotto.append(temp)

print(f"the lottery numbers are: {temp}")
for i in lotto :
    print(f"{(i):4d}")
print()


