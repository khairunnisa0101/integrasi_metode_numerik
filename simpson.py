import numpy as np
import time

#Mendefinisikan fungsi simson_integral
def simpson_integral(f, a, b, N):
    if N % 2 == 1:
        raise ValueError("N harus genap")
    
    h = (b - a) / N
    x = np.linspace(a, b, N + 1)
    fx = f(x)
    
    integral = fx[0] + fx[-1]
    integral += 4 * np.sum(fx[1:N:2])
    integral += 2 * np.sum(fx[2:N-1:2])
    
    integral *= h / 3
    return integral

def f(x):
    return 4 / (1 + x**2)

# Nilai referensi phi
phi_reference = 3.14159265358979323846

# Variasi nilai N
Ns = [10, 100, 1000, 10000]

# Testing kode dan pengukuran waktu eksekusi serta galat RMS
results = []
for N in Ns:
    start_time = time.time()
    integral_value = simpson_integral(f, 0, 1, N)
    end_time = time.time()
    
    elapsed_time = end_time - start_time
    rms_error = np.sqrt((integral_value - phi_reference) ** 2)
    
    results.append((N, integral_value, rms_error, elapsed_time))

# Menampilkan hasil
for result in results:
    print(f"N = {result[0]}")
    print(f"Nilai integral = {result[1]}")
    print(f"Galat RMS = {result[2]}")
    print(f"Waktu eksekusi = {result[3]} detik")
    print("-" * 30)
