import math

# Step ratio factor: 12th root of 2
factor = 2 ** (1 / 12)

# F# is 6 steps away from C (C -> C# -> D -> D# -> E -> F -> F#)
steps = 6

# Ratio of frequencies: f(F#) / f(C)
ratio = factor**steps

print(f"Calculated Ratio: {ratio:.6f}")
print(f"sqrt(2) Value:    {math.sqrt(2):.6f}")
