error = 0.00000000001

def F(x):
    return (x-1)**2*(x-2)*(x-3)

def FT(x):
    return 2*(x-1)*(x-2)*(x-3) + (x-1)**2*(2*x-5)

x0 = 0
i = 0

print("Starting point for the method= {:.6f}".format(x0))

while True:
    x = x0
    x0 = x - F(x) / FT(x)
    i += 1
    print("{:d}. step, approximate value= {:.6f}".format(i, x0))

    if abs(x0 - x) <= error:
        break

print("Approximate root = {:.6f}".format(x0))
