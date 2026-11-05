import numpy as np

# 1. Given Data
sp = 192               # Selling price per kg (₹)
profit_pct = 0.08      # 8% profit
cp_p = 800 / 5         # Cost price of variety P = ₹ 160/kg
cp_q = 800 / 4         # Cost price of variety Q = ₹ 200/kg

# 2. Derivation of Mixture Cost Price (CP_mix)
# Formula: SP = CP * (1 + profit) => CP_mix = SP / (1 + profit)
cp_mix = sp / (1 + profit_pct)
print(f"Derived Mixture Cost Price (CP_mix) = {cp_mix:.2f} ₹/kg")

# 3. Derivation of Alligation Rule:
# Let W_P and W_Q be weights. Total Cost = W_P * cp_p + W_Q * cp_q = (W_P + W_Q) * cp_mix
# W_P * (cp_mix - cp_p) = W_Q * (cp_q - cp_mix)
# W_P / W_Q = (cp_q - cp_mix) / (cp_mix - cp_p)

diff_q = cp_q - cp_mix       # 200 - 177.77 = 22.22
diff_p = cp_mix - cp_p       # 177.77 - 160 = 17.77

ratio_p_to_q = diff_q / diff_p
print(f"Alligation Calculation:")
print(f"  (C_Q - CP_mix) = {cp_q} - {cp_mix:.2f} = {diff_q:.2f}")
print(f"  (CP_mix - C_P) = {cp_mix:.2f} - {cp_p} = {diff_p:.2f}")
print(f"Weight Ratio W_P : W_Q = {diff_q:.2f} / {diff_p:.2f} = 5 : 4")