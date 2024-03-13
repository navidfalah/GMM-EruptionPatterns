import matplotlib.pyplot as plt
from scipy.stats import multivariate_normal
import numpy as np

# Redefine the parameters based on the provided image
mix_ratio_1 = 0.45  # Slightly less than half of the points seem to be yellow
mix_ratio_2 = 0.55  # Slightly more than half of the points seem to be purple

# Estimates for the mean values based on the image
mean_1 = [2.5, 55]  # Yellow cluster
mean_2 = [4.5, 80]  # Purple cluster

# Estimates for the covariance matrices based on the spread of the points in the image
# Yellow cluster is more spread in the x-axis and less in y-axis
covariance_1 = [[0.3, 0], [0, 20]]
# Purple cluster is less spread in the x-axis and more in y-axis
covariance_2 = [[0.1, 0], [0, 30]]

# Number of samples to generate
num_samples = 1000

# Samples allocation according to mix ratios
num_samples_1 = int(num_samples * mix_ratio_1)
num_samples_2 = num_samples - num_samples_1

# Generating samples for each component
samples_1 = np.random.multivariate_normal(mean_1, covariance_1, num_samples_1)
samples_2 = np.random.multivariate_normal(mean_2, covariance_2, num_samples_2)

# Combine the samples to form the complete dataset
data = np.concatenate((samples_1, samples_2), axis=0)

# Shuffle the dataset to mix the samples from the two components
np.random.shuffle(data)

# Scatter plot of the generated data
plt.figure(figsize=(8, 6))
plt.scatter(data[:, 0], data[:, 1], c=np.linspace(0, 1, num_samples), cmap='viridis')
plt.colorbar(label='Component mix ratio')
plt.xlabel('Eruption time (min)')
plt.ylabel('Time to next eruption (min)')
plt.title('Simulated Eruption Data')
plt.show()
