n = int(input('Dame n: '))

factorial = 1
for i in range(1, n + 1):
    factorial = factorial * i

print(f'{n}! = {factorial}')
