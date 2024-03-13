from scipy.stats import norm
from parameters import (mix_ratio_1, mix_ratio_2,
mean_1, mean_2, covariance_1, covariance_2)

# Part C: Updated Probability for Component 1 Given Observed Eruption Time

# GMM Parameters
mix_ratio_1, mix_ratio_2 = 0.356, 0.644  # Prior probabilities of each component
mean_1, mean_2 = [2.04, 54.5], [4.29, 80.0]  # Means of each component
covariance_1 = [[0.0693, 0.436], [0.436, 33.7]]  # Covariance matrix for component 1
covariance_2 = [[0.170, 0.939], [0.939, 36.0]]  # Covariance matrix for component 2

# Observed data
observed_eruption_time = 3  # Observed eruption time in minutes

# Calculate the likelihood of the observed eruption time under each component
# This uses the normal distribution defined by the first element of each component's mean and the square root of the first element of each component's covariance matrix
likelihood_1 = norm(mean_1[0], covariance_1[0][0]**0.5).pdf(observed_eruption_time)
likelihood_2 = norm(mean_2[0], covariance_2[0][0]**0.5).pdf(observed_eruption_time)

# Update the probability for component 1
# This calculation uses Bayes' Theorem to update the probability of component 1 based on the observed eruption time
updated_probability_1 = (likelihood_1 * mix_ratio_1) / ((likelihood_1 * mix_ratio_1) + (likelihood_2 * mix_ratio_2))

# Display the updated probability for component 1
print(f"Updated probability for component 1: {updated_probability_1:.3f}")
