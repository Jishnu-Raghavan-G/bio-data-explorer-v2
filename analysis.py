import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("sample_data.csv")

# Separate data
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

# Create bar graph
plt.bar(labels, values, color=["green", "red"])

# Add labels and title
plt.title("Healthy vs Disease Expression")
plt.xlabel("Condition")
plt.ylabel("Average Expression")

# Save the graph (important for GitHub)
plt.savefig("output.png")

# Show the graph
plt.show()
