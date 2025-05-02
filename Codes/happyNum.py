num = int(input("Enter a number: "))

for i in range(num):
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit * digit
        temp //= 10
    if sum == 1:
        print("It is a happy number")
        break
    num = sum
else:
    print("It is not a happy number")
