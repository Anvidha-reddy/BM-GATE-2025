def calculate_total_bill(C):
    """Calculates total bill given consulting fee C."""
    if C <= 500000:
        overhead = 0.20 * C
    else:
        overhead = 100000 + 0.10 * (C - 500000)

    total_amount = C + overhead
    tax = 0.18 * total_amount
    grand_total = total_amount + tax
    return grand_total

# Formula derived for C > 5,000,000:
# Grand Total = 1.18 * (1.1 * C + 50000)
# Setting Grand Total = 1,000,000:
max_total = 1000000
C_exact = (max_total / 1.18 - 50000) / 1.1

print(f"Calculated Consulting Fee: ₹{C_exact:.2f}")
print(f"Rounded Consulting Fee: ₹{round(C_exact):,}")

# Verify against options provided
options = {
    "(A)": 701438,
    "(B)": 724961,
    "(C)": 751232,
    "(D)": 775784
}

print("\n--- Option Verification ---")
for label, val in options.items():
    print(f"Option {label} ₹{val:,} -> Total Bill = ₹{calculate_total_bill(val):,.2f}")
