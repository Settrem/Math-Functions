
import numpy as np

# Mata in stickprovet
x = list(map(float, input("Ange stickprovet (separera med mellanslag): ").split()))

n = len(x)
x_bar = np.mean(x)

print(f"Stickprovsmedelvärde: {x_bar:.4f}")

val = input("Är väntevärdet känt (j) eller okänt (n)? ").lower()

if val == "j":
    mu = float(input("Ange det kända väntevärdet: "))
    varians = sum((xi - mu)**2 for xi in x) / n

elif val == "n":
    mu = x_bar
    varians = sum((xi - mu)**2 for xi in x) / (n - 1)
    print(f"Skattat väntevärde: {mu:.4f}")

else:
    print("Felaktigt val!")
    exit()

standardavvikelse = np.sqrt(varians)

print(f"Varians: {varians:.4f}")
print(f"Standardavvikelse: {standardavvikelse:.4f}")
