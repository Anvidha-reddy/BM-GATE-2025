import sympy as sp

# Define probabilities as symbolic variables
P_A, P_B, P_A_intersect_B = sp.symbols('P_A P_B P_A_intersect_B', positive=True)

# Condition: B is a subset of A (B \subset A), which means A \cap B = B
P_A_intersect_B_cond = P_B

# Definition of Conditional Probability: P(A|B) = P(A \cap B) / P(B)
P_A_given_B_formula = P_A_intersect_B / P_B

# Substitute the subset condition into the formula
P_A_given_B = P_A_given_B_formula.subs(P_A_intersect_B, P_A_intersect_B_cond)
final_result = sp.simplify(P_A_given_B)

print(f"Derived Conditional Probability P(A|B) when B subset of A: {final_result}")
