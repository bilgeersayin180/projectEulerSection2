

def fact(n):
    if ((n == 1) or (n == 0)):
        return 1
    else: 
        return n * fact(n - 1)

def c(N,R):
    return (fact(N) / (fact(N - R) * fact(R)))

times = 0

for i in range(1, 101):
    for j in range(1, i + 1):
        if (c(i,j) > 1000000):
            times += 1

print(times)


