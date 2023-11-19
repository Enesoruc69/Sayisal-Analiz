import math

def f(x):
    return 4 * math.exp(-0.5 * x) - x

x = 2  # Başlangıç değeri
epsilon = 1e-6  # Hata payı
iteration = 4  # İterasyon sayısı

for i in range(iteration):
    fx = f(x)
    derivative = -2 * math.exp(-0.5 * x) - 1

    if abs(fx) < epsilon:
        print("Bulunan çözüm:", x)
        break

    x = x - fx / derivative
    print(f"Iterasyon {i + 1} çözüm: {x}")