def print_narcissistic_numbers(n):
    for num in range(10**(n-1), 10**n):
        sum = 0
        temp = num
        while temp > 0:
            digit = temp % 10
            sum += digit ** n
            temp //= 10
        if num == sum:
            print(num)

# 调用函数打印3位数的水仙花数
print_narcissistic_numbers(3)
# 调用函数打印4位数的水仙花数
print_narcissistic_numbers(4)

