import pandas as pd

# Data from the table
data = {
    'Nation': ['USA', 'Canada', 'Japan', 'Australia', 'France'],
    'Gold': [40, 39, 20, 17, 16],
    'Silver': [44, 27, 12, 19, 26],
    'Bronze': [41, 24, 13, 16, 22]
}

# Create DataFrame
df = pd.DataFrame(data)

# Calculate total medals for each nation
df['Total'] = df['Gold'] + df['Silver'] + df['Bronze']

# Total medals across all 5 nations
grand_total = df['Total'].sum()

# Sort by Total medals to check ranking
df_by_total = df.sort_values(by='Total', ascending=False).reset_index(drop=True)

# Statement A check: France position in total medals ranking
france_rank = df_by_total[df_by_total['Nation'] == 'France'].index[0] + 1

# Statement B check: Top two nations by total medals
top_2_gold_rank = list(df['Nation'].iloc[:2])
top_2_total_rank = list(df_by_total['Nation'].iloc[:2])

# Statement C check: USA + Canada percentage of total medals in table
usa_canada_total = df[df['Nation'].isin(['USA', 'Canada'])]['Total'].sum()
usa_canada_pct = (usa_canada_total / grand_total) * 100

# Statement D check: Ratio of Canada total medals to Japan total medals
canada_total = df[df['Nation'] == 'Canada']['Total'].values[0]
japan_total = df[df['Nation'] == 'Japan']['Total'].values[0]
ratio = canada_total / japan_total

# Output calculations
print("--- Data Table with Total Medals ---")
print(df[['Nation', 'Gold', 'Silver', 'Bronze', 'Total']])
print("\n--- Statement Verification ---")
print(f"Statement A: France is ranked #{france_rank} by total medals.")
print(f"Statement B: Top 2 by Gold = {top_2_gold_rank}, Top 2 by Total = {top_2_total_rank}")
print(f"Statement C: USA + Canada total = {usa_canada_total}/{grand_total} ({usa_canada_pct:.2f}%)")
print(f"Statement D: Canada ({canada_total}) vs Japan ({japan_total}) -> Ratio = {ratio:.2f}")
