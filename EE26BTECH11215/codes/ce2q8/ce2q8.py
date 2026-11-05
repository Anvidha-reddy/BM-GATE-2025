import itertools

# Problem 3.3: PQRST distinct digits (1 to 5) satisfying P < Q, S > P > T, R < T
# Problem 8: Five-digit number puzzle using manual loops instead of itertools
digits = [1, 2, 3, 4, 5]
solutions = []

for p in digits:
    for q in digits:
        if q == p:
            continue
        for r in digits:
            if r == p or r == q:
                continue
            for s in digits:
                if s == p or s == q or s == r:
                    continue
                for t in digits:
                    if t == p or t == q or t == r or t == s:
                        continue
                    # Conditions: P < Q, S > P > T, R < T
                    if p < q and s > p > t and r < t:
                        solutions.append((p, q, r, s, t))

for sol in solutions:
    print(f"P={sol[0]}, Q={sol[1]}, R={sol[2]}, S={sol[3]}, T={sol[4]}")

# Alternative solution using python libraries
'''
# Digits 1 through 5
digits = [1, 2, 3, 4, 5]

# Generate all possible 5-digit permutations with distinct digits
for P, Q, R, S, T in itertools.permutations(digits):
  # Check the conditions given in the problem:
  # 1. P < Q
  # 2. S > P > T  (i.e., S > P and P > T)
  # 3. R < T
  if P < Q and (S > P and P > T) and R < T:
    print(f"Valid digits found -> P: {P}, Q: {Q}, R: {R}, S: {S}, T: {T}")
    print(f"The value of P is: {P}")
'''
