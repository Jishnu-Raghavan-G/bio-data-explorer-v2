import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("d:/bio-data-explorer-v2/sample_data.csv")

# Separate data into healthy and diseased
healthy = df[df["condition"] == "healthy"]
disease = df[df["condition"] == "disease"]

# Calculate mean expression
healthy_mean = healthy["expression"].mean()
disease_mean = disease["expression"].mean()

# Print results
print("Healthy mean:", healthy_mean)
print("Disease mean:", disease_mean)

# Prepare data for plotting
labels = ["Healthy", "Disease"]
values = [healthy_mean, disease_mean]

# Create plot
plt.figure(figsize=(6, 4))
colors = ["#4CAF50", "#F44336"]  # softer green & red

bars = plt.bar(labels, values, color=colors)

# Title and labels
plt.title("Healthy vs Disease Gene Expression", fontsize=14)
plt.xlabel("Condition")
plt.ylabel("Average Expression")

# Add value labels on bars
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval,
             round(yval, 2),
             ha='center', va='bottom', fontsize=10)

# Clean layout
plt.tight_layout()

# Save the figure (IMPORTANT for LinkedIn)
plt.savefig("gene_expression_plot.png", dpi=300)

# Show plot
plt.show()
