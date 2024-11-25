def fibonacci(n):
    if n<=1:
        return n
    else:
        return(fibonacci(n-1)+fibonacci(n-2))
item=int(input())

for i in range(item):
    print(fibonacci(i))

