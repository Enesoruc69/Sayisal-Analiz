def bisection(x):
    return x * x * x - 2 * x * x - 5


x1 = 2
x2 = 4
x0 = float
y0 = float
a = bisection(x1)
b = bisection(x2)

for i in range(4):
    if a * b < 0:
        x0 = (x1 + x2)/2
        y0 = bisection(x0)
        if y0 * a < 0:
            x2 = x0
        elif y0 * b < 0:
            x1 = x0
    print("{}.İterasyon".format(i+1))
    print("x in degeri : {}".format(x0))
    print("f(x) in degeri : {:.15f}".format(y0))
    print()