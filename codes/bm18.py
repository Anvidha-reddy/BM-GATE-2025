binary = "10110111"

# Number of bits
n = len(binary)

# Convert binary to decimal
D = int(binary, 2)

# Reference voltage
Vref = 5

# DAC output
Vout = (D / (2**n - 1)) * Vref

print("Decimal value =", D)
print("DAC output =", round(Vout, 2), "V")
