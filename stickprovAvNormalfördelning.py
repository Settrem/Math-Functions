
import numpy as np

# Ange normalfördelningen N(mu, sigma)
mu = float(input("Ange väntevärdet mu: "))
sigma = float(input("Ange standardavvikelsen sigma: "))
n = int(input("Ange antal observationer n: "))

# Generera stickprovet
x = np.random.normal(mu, sigma, n)

# Beräkna stickprovsmedelvärdet
x_bar = np.mean(x)

print("\nStickprov:")
print(x)

print(f"\nStickprovsmedelvärde: {x_bar:.4f}")
