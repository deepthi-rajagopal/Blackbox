import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the two CSV files into Pandas DataFrames
file1 = r"C:\Users\I584341\c1.csv" 
file2 = r"C:\Users\I584341\cn.csv"

df1 = pd.read_csv(file1)
df2 = pd.read_csv(file2)

# Compare the DataFrames to find differences
changed_cells = []

for col in df1.columns:
    for i, (val1, val2) in enumerate(zip(df1[col], df2[col])):
        if val1 != val2:
            changed_cells.append({
                'Column': col,
                'Row': i + 1,  # Adding 1 because row indices start from 1
                'Value1': val1,
                'Value2': val2
            })

# Create a DataFrame to store the changed cells
df_changes = pd.DataFrame(changed_cells)

# Print the details of changed cells
print("Changed Cells:")
print(df_changes)

# Save the changes to a new CSV file
output_file = r"C:\Users\I584341\changesq1.csv"
df_changes.to_csv(output_file, index=False)

print(f"Changes saved to '{output_file}'")

# Visualize the changes with a scatter plot
# Load the CSV file into a Pandas DataFrame
csv_file = r"C:\Users\I584341\changesq1.csv"
df = pd.read_csv(csv_file)

# Specify the two columns you want to plot
x_column = 'Value1'  
y_column = 'Value2'  

# Create a scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(df[x_column], df[y_column], marker='o', s=50, c='blue', alpha=0.7)
plt.xlabel("Initial")
plt.ylabel("End")
plt.title(f'Scatter Plot of Intial vs. End')
plt.grid(True)
plt.tight_layout()

# Show the plot
plt.show()

