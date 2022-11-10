# bucle for

nums = [1,2,3,4,5,6,7,8,9,10]

for num in nums:
    if num == 5:
        break
    print(num)

for num in nums:
    if num == 5:
        continue
    print(num)

for number in range(1,8):
    print(number)

for letra in 'hello':
    print(letra)


# bucle while

count = 4

while count <= 10:
    print(count)
    count = count + 1
    count += count
