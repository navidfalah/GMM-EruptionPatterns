import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import multivariate_normal, norm

# Define the simulation parameters
mix_ratio_1, mix_ratio_2 = 0.356, 0.644
mean_1, mean_2 = [2.04, 54.5], [4.29, 80.0]
covariance_1, covariance_2 = [[0.0693, 0.436], [0.436, 33.7]], [[0.170, 0.939], [0.939, 36.0]]

def generate_dataset():
    """Generate a dataset based on the Gaussian Mixture Model parameters."""
    samples_1 = np.random.multivariate_normal(mean_1, covariance_1, int(mix_ratio_1 * 1000))
    samples_2 = np.random.multivariate_normal(mean_2, covariance_2, int(mix_ratio_2 * 1000))
    data = np.concatenate((samples_1, samples_2), axis=0)
    np.random.shuffle(data)
    return data

def plot_data(data):
    """Plot the generated dataset."""
    plt.figure(figsize=(8, 6))
    plt.scatter(data[:, 0], data[:, 1], c=np.linspace(0, 1, len(data)), cmap='viridis')
    plt.colorbar(label='Component mix ratio')
    plt.xlabel('Eruption time (min)')
    plt.ylabel('Time to next eruption (min)')
    plt.title('Simulated Eruption Data')
    plt.show()

def calculate_mahalanobis_distance(x, mean, cov):
    """Calculate the Mahalanobis distance."""
    x_minus_mu = x - mean
    inv_covmat = np.linalg.inv(cov)
    left_term = np.dot(x_minus_mu, inv_covmat)
    mahal = np.dot(left_term, x_minus_mu.T)
    return mahal.diagonal()

def analyze_eruptions(data):
    """Analyze the dataset to calculate the number of eruptions from each component."""
    # This example uses the entire dataset for analysis; adjust as needed for specific samples
    dist_to_1 = calculate_mahalanobis_distance(data[:, :2], mean_1, covariance_1)
    dist_to_2 = calculate_mahalanobis_distance(data[:, :2], mean_2, covariance_2)
    assignments = dist_to_1 < dist_to_2
    num_eruptions_1 = np.sum(assignments)
    num_eruptions_2 = len(assignments) - num_eruptions_1
    print(f"Eruptions from Component 1: {num_eruptions_1}, Component 2: {num_eruptions_2}")
    return num_eruptions_1, num_eruptions_2

def calculate_probability_within_conditions(data):
    """Calculate the probability within specific conditions."""
    condition = (data[:, 0] >= 3) & (data[:, 0] <= 4) & (data[:, 1] >= 60) & (data[:, 1] <= 70)
    probability = np.mean(condition)
    print(f"Probability within conditions: {probability:.3f}")
    return probability

def calculate_updated_probability(observed_eruption_time=3):
    """Calculate the updated probability for component 1."""
    likelihood_1 = norm(mean_1[0], np.sqrt(covariance_1[0][0])).pdf(observed_eruption_time)
    likelihood_2 = norm(mean_2[0], np.sqrt(covariance_2[0][0])).pdf(observed_eruption_time)
    updated_prob_1 = (likelihood_1 * mix_ratio_1) / (likelihood_1 * mix_ratio_1 + likelihood_2 * mix_ratio_2)
    print(f"Updated probability for component 1: {updated_prob_1:.3f}")
    return updated_prob_1

def simulate_conditional_distribution(num_samples=500, observed_eruption_time=3, updated_probability_1=None):
    """Simulate the conditional distribution for the time until the next eruption."""
    if updated_probability_1 is None:
        updated_probability_1 = calculate_updated_probability(observed_eruption_time)
    # Calculate conditional means and variances
    conditional_means = [mean_1[1] + (covariance_1[0][1] / np.sqrt(covariance_1[0][0])) * (observed_eruption_time - mean_1[0]),
                         mean_2[1] + (covariance_2[0][1] / np.sqrt(covariance_2[0][0])) * (observed_eruption_time - mean_2[0])]
    conditional_variances = [covariance_1[1][1] * (1 - (covariance_1[0][1]**2 / (covariance_1[0][0] * covariance_1[1][1]))),
                             covariance_2[1][1] * (1 - (covariance_2[0][1]**2 / (covariance_2[0][0] * covariance_2[1][1])))]
    # Simulate times for both components
    simulated_times_1 = norm(conditional_means[0], np.sqrt(conditional_variances[0])).rvs(num_samples)
    simulated_times_2 = norm(conditional_means[1], np.sqrt(conditional_variances[1])).rvs(num_samples)
    # Calculate probabilities based on simulations
    simulated_prob_1 = np.mean(simulated_times_1 < 60)
    simulated_prob_2 = np.mean(simulated_times_2 < 60)
    # Combine probabilities using the updated probability for component 1
    combined_prob = updated_probability_1 * simulated_prob_1 + (1 - updated_probability_1) * simulated_prob_2
    print(f"Conditional probability for next eruption < 60 mins: {combined_prob:.3f}")
    return combined_prob

# Generate dataset and perform analysis
# data = generate_dataset()
# plot_data(data)
# analyze_eruptions(data)
# calculate_probability_within_conditions(data)
# updated_prob_1 = calculate_updated_probability()
# simulate_conditional_distribution(500, 3, updated_prob_1)
