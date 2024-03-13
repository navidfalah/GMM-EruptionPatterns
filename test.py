import matplotlib.pyplot as plt
from scipy.stats import multivariate_normal
import numpy as np
from scipy.stats import norm

# Redefine the parameters based on the provided image
mix_ratio_1 = 0.356 # Slightly less than half of the points seem to be yellow
mix_ratio_2 = 0.644  # Slightly more than half of the points seem to be purple

# Estimates for the mean values based on the image
mean_1 = [2.04, 54.5]  # Yellow cluster
mean_2 = [4.29, 80.0] # Purple cluster

# Estimates for the covariance matrices based on the spread of the points in the image
# Yellow cluster is more spread in the x-axis and less in y-axis
# Purple cluster is less spread in the x-axis and more in y-axis
covariance_1 = [[0.0693, 0.436], [0.436, 33.7]]
covariance_2 = [[0.170, 0.939], [0.939, 36.0]]

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

# Function to calculate Mahalanobis distance

def mahalanobis_distance(x, mean, cov):

    x_minus_mu = x - mean

    inv_covmat = np.linalg.inv(cov)

    left_term = np.dot(x_minus_mu, inv_covmat)

    mahal = np.dot(left_term, x_minus_mu.T)

    return mahal.diagonal()


# Simulating the observation of 100 random eruptions from the dataset to calculate the number of eruptions
# from component 1 and component 2 based on the random data.

# Randomly selecting 100 eruptions from the dataset
random_selection_indices_100 = np.random.choice(data.shape[0], size=100, replace=False)
random_selected_eruptions_100 = data[random_selection_indices_100]

# Calculate distances to each cluster for the 100 eruptions
dist_to_1_100 = mahalanobis_distance(random_selected_eruptions_100, mean_1, covariance_1)
dist_to_2_100 = mahalanobis_distance(random_selected_eruptions_100, mean_2, covariance_2)

# Assignments to nearest cluster for the 100 eruptions
assignments_100 = dist_to_1_100 < dist_to_2_100

# Count eruptions from each component for the 100 eruptions
num_eruptions_1_100 = np.sum(assignments_100)
num_eruptions_2_100 = len(assignments_100) - num_eruptions_1_100

print(num_eruptions_1_100)
print(num_eruptions_2_100)

# question b
num_samples = 1000
samples_1 = np.random.multivariate_normal(mean_1, covariance_1, int(num_samples * mix_ratio_1))
samples_2 = np.random.multivariate_normal(mean_2, covariance_2, num_samples - int(num_samples * mix_ratio_1))
data_samples = np.concatenate((samples_1, samples_2), axis=0)

time_conditions_samples = (data_samples[:, 0] >= 3) & (data_samples[:, 0] <= 4) & (data_samples[:, 1] >= 60) & (data_samples[:, 1] <= 70)
probability_within_conditions_samples = np.mean(time_conditions_samples)



print(probability_within_conditions_samples)

# part c
# Re-running the simulation with 1000 random observed eruption times to calculate the updated probability for component 1.


def calculate_likelihood(observed_eruption_time):

    likelihood_1 = norm(mean_1[0], covariance_1[0][0]**0.5).pdf(observed_eruption_time)

    likelihood_2 = norm(mean_2[0], covariance_2[0][0]**0.5).pdf(observed_eruption_time)

    return likelihood_1, likelihood_2

def update_probability(likelihood_1, likelihood_2):

    updated_probability_1 = (likelihood_1 * mix_ratio_1) / ((likelihood_1 * mix_ratio_1) + (likelihood_2 * mix_ratio_2))

    return updated_probability_1


observed_eruption_time_single = 3  # Observed time of 3 minutes



# Calculate likelihood and updated probability for the single observed time

likelihood_1_single, likelihood_2_single = calculate_likelihood(observed_eruption_time_single)

updated_probability_1_single = update_probability(likelihood_1_single, likelihood_2_single)

print(updated_probability_1_single)

# question d


