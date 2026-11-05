# Code by Nehan Mohammad
# Gate 2025, Civil Engineering, question 3.

# Given Parameters
cost = 7/1000
powrat = 40
hours1 = 10
hours2 = 12
days = 180

# Calculate cost
total_cost = powrat*hours1*days*cost

# Calculating percentage-increase
new_cost = powrat*hours2*days*cost
diff = new_cost - total_cost
perct = (diff/total_cost)*100

print(f" Initial charge value:{cost*1000}₹ per kWh,\n Power consumed by a desklight: {powrat}, \n Number of hours turned on each day: {hours1}, \n Number of days: {days}")
print(f"Cost of energy consumption: {total_cost:.2f}")
print(f"Percentage-increase in cost of energy consumption: {perct:.2f}")

