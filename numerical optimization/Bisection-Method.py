import math

hata = 0.002

def F(x):
    return math.sin(x) + math.cos(x) - x

a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))

if F(a) * F(b) >= 0:
    print("No root exists between {:.4f} and {:.4f}.".format(a, b))
else:
    x0 = (a + b) / 2
    i = 0

    while True:
        i += 1
        print("{:d}. step, approximate root= {:.4f}\t ".format(i, x0), end='')

        x1 = x0
        if F(x0) * F(a) < 0:
            b = x0
        else:
            a = x0

        print("new interval= [{:.4f}, {:.4f}]".format(a, b))

        x0 = (a + b) / 2

        if abs(x0 - x1) <= hata:
            break

    print("{:d}. step, exited from the loop. Approximate root in step {:d}= {:.4f}".format(i + 1, i + 1, x0))
    print("{:.3f} error, approximate root = {:.4f}".format(hata, x0))
    print("f({:.4f})= {:.3f}".format(x0, F(x0)))
