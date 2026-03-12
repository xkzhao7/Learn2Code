# Mutation Detective: Probabilistic Detection of Real DNA Mutations
# Uses TCGA MC3 open-access mutation dataset

import pandas as pd
import numpy as np
from scipy.stats import binom
import matplotlib.pyplot as plt

# ----------------------------
# 1. Load TCGA MC3 dataset
# ----------------------------

file_path = "/Users/xkzhao/Downloads/mc3.v0.2.8.PUBLIC.maf.gz"

data = pd.read_csv(file_path, sep="\t", comment="#", low_memory=False)

# Keep relevant columns
data = data[["Hugo_Symbol", "t_depth", "t_alt_count"]]

# Rename for convenience
data = data.rename(columns={
    "Hugo_Symbol": "gene",
    "t_depth": "n",
    "t_alt_count": "k"
})

# Remove rows with missing read counts
data = data.dropna()

# Convert to integers
data["n"] = data["n"].astype(int)
data["k"] = data["k"].astype(int)

# Optional: use a smaller subset for faster experimentation
data = data.sample(1000, random_state=42)

# ----------------------------
# 2. Bayesian mutation detector
# ----------------------------

def mutation_probability(k, n, error_rate=0.001, mutation_fraction=0.3, prior=0.001):

    p_data_given_mut = binom.pmf(k, n, mutation_fraction)
    p_data_given_noise = binom.pmf(k, n, error_rate)

    numerator = p_data_given_mut * prior
    denominator = numerator + p_data_given_noise * (1 - prior)

    return numerator / denominator

# Apply model
data["P_real_mutation"] = data.apply(
    lambda row: mutation_probability(row["k"], row["n"]),
    axis=1
)

# ----------------------------
# 3. Compute mutation fraction
# ----------------------------

data["mutation_fraction"] = data["k"] / data["n"]

# ----------------------------
# 4. Show example results
# ----------------------------

print(data.head(10))

# ----------------------------
# 5. Visualization
# ----------------------------

plt.scatter(data["mutation_fraction"], data["P_real_mutation"], alpha=0.5)

plt.xlabel("Observed Mutation Fraction (k/n)")
plt.ylabel("Probability Mutation Is Real")
plt.title("Bayesian Detection of Real Mutations")

plt.show()