from scipy.stats import multivariate_normal, norm

# Set parameters for Gaussian Mixture Model (GMM)
mix_ratio_1, mix_ratio_2 = 0.356, 0.644
mean_1, mean_2 = [2.04, 54.5], [4.29, 80.0]
covariance_1 = [[0.0693, 0.436], [0.436, 33.7]]
covariance_2 = [[0.170, 0.939], [0.939, 36.0]]

# Calculate expected number of eruptions for each component from 10 total eruptions
expected_eruptions_1 = 10 * mix_ratio_1
expected_eruptions_2 = 10 * mix_ratio_2

# Calculate the probability of an eruption duration between 3-4 minutes and the following one between 60-70 minutes
bounds_start, bounds_end = [3, 60], [4, 70]
probability_1 = multivariate_normal(mean_1, covariance_1).cdf(bounds_end) - multivariate_normal(mean_1, covariance_1).cdf(bounds_start)
probability_2 = multivariate_normal(mean_2, covariance_2).cdf(bounds_end) - multivariate_normal(mean_2, covariance_2).cdf(bounds_start)
combined_probability = mix_ratio_1 * probability_1 + mix_ratio_2 * probability_2

# Compute the updated likelihood of component 1 given an observed eruption time of 3 minutes
observed_eruption_time = 3
likelihood_1 = norm(mean_1[0], covariance_1[0][0]**0.5).pdf(observed_eruption_time)
likelihood_2 = norm(mean_2[0], covariance_2[0][0]**0.5).pdf(observed_eruption_time)
updated_probability_1 = (likelihood_1 * mix_ratio_1) / (likelihood_1 * mix_ratio_1 + likelihood_2 * mix_ratio_2)

# Determine the conditional probability of the next eruption occurring in less than 60 minutes given an initial 3-minute eruption
conditional_mean_1 = mean_1[1] + (covariance_1[0][1] / covariance_1[0][0]**0.5) * (observed_eruption_time - mean_1[0])
conditional_variance_1 = covariance_1[1][1] * (1 - (covariance_1[0][1] / (covariance_1[0][0] * covariance_1[1][1]))**2)
conditional_probability_1 = norm(conditional_mean_1, conditional_variance_1**0.5).cdf(60)

conditional_mean_2 = mean_2[1] + (covariance_2[0][1] / covariance_2[0][0]**0.5) * (observed_eruption_time - mean_2[0])
conditional_variance_2 = covariance_2[1][1] * (1 - (covariance_2[0][1] / (covariance_2[0][0] * covariance_2[1][1]))**2)
conditional_probability_2 = norm(conditional_mean_2, conditional_variance_2**0.5).cdf(60)

updated_probability_2 = 1 - updated_probability_1
combined_conditional_probability = updated_probability_1 * conditional_probability_1 + updated_probability_2 * conditional_probability_2

# Summarize results
results = {
    "Expected eruptions from component 1": expected_eruptions_1,
    "Expected eruptions from component 2": expected_eruptions_2,
    "Probability of specified eruption durations": combined_probability,
    "Updated probability for component 1": updated_probability_1,
    "Conditional probability for next eruption < 60 mins": combined_conditional_probability
}

print(results)
