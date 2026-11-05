# Forward Pass (Earliest Event Times)
TE1 = 0
TE2 = TE1 + 3  # Activity A
TE3 = TE1 + 5  # Activity C
TE4 = max(TE2 + 5, TE3 + 2)  # Activities B and D
TE5 = max(TE4 + 4, TE3 + 8)  # Activities E and F

# Backward Pass (Latest Event Times)
TL5 = TE5
TL4 = TL5 - 4  # Activity E
TL3 = min(TL4 - 2, TL5 - 8)  # Activities D and F
TL2 = TL4 - 5  # Activity B

# Total float for Activity E (4 -> 5, duration = 4)
t_E = 4
TF_E = TL5 - TE4 - t_E

print(f"Total float available for activity E: {TF_E}")
