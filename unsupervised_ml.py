
# Import the required libraries
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Customer data: [monthly spending, monthly visits]
customers = [
    [1000, 2], [1500, 3], [2000, 2],
    [5000, 6], [6000, 7], [5500, 5],
    [12000, 12], [15000, 14], [13000, 11],
    [3000, 4]
]

# Scale the data
scaler = StandardScaler()
data = scaler.fit_transform(customers)

# Create and train the K-Means model
model = KMeans(n_clusters=3, random_state=42, n_init=10)
clusters = model.fit_predict(data)

# Display each customer's cluster
for i in range(len(customers)):
    print("Customer", i + 1, "belongs to Cluster", clusters[i])

# Count customers in each cluster
print("\nCustomers in each cluster:")

for i in range(3):
    print("Cluster", i, ":", list(clusters).count(i), "customers")

# Draw the customer groups (bonus task)
plt.scatter(
    [c[0] for c in customers],
    [c[1] for c in customers],
    c=clusters,
    cmap="viridis"
)

plt.xlabel("Monthly Spending (KES)")
plt.ylabel("Monthly Visits")
plt.title("Customer Segmentation")
plt.show()
