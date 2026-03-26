import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("sample_data.csv")

# Separate data
healthy = df[df["condition"] == "healthy"]
disease = df[df["condition"] == "disease"]

# Mean expression
healthy_mean = healthy["expression"].mean()
disease_mean = disease["expression"].mean()

# Print values
print("Healthy mean:", healthy_mean)
print("Disease mean:", disease_mean)

# Plot comparison
labels = ["Healthy", "Disease"]
values = [healthy_mean, disease_mean]

plt.bar(labels, values)
plt.title("Healthy vs Disease Expression")
plt.xlabel("Condition")
plt.ylabel("Average Expression")
plt.show()