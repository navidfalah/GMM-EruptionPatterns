from scipy.stats import norm
from parameters import (mean_1, mean_2, covariance_1, covariance_2)
# Part D: Conditional Probability of Next Eruption Occurring in Less than 60 Minutes

# GMM Parameters and Observed Eruption Time
observed_eruption_time = 3
updated_probability_1 = 0.130  # Assuming this value is derived from part C

# Compute conditional means and variances
conditional_mean_1 = mean_1[1] + (covariance_1[0][1] / covariance_1[0][0]**0.5) * (observed_eruption_time - mean_1[0])
conditional_variance_1 = covariance_1[1][1] * (1 - (covariance_1[0][1]**2 / (covariance_1[0][0] * covariance_1[1][1])))
conditional_probability_1 = norm(conditional_mean_1, conditional_variance_1**0.5).cdf(60)

conditional_mean_2 = mean_2[1] + (covariance_2[0][1] / covariance_2[0][0]**0.5) * (observed_eruption_time - mean_2[0])
conditional_variance_2 = covariance_2[1][1] * (1 - (covariance_2[0][1]**2 / (covariance_2[0][0] * covariance_2[1][1])))
conditional_probability_2 = norm(conditional_mean_2, conditional_variance_2**0.5).cdf(60)

# Assuming part C correctly identifies component 1, adjust for mixture component probabilities
combined_conditional_probability = updated_probability_1 * conditional_probability_1 + (1 - updated_probability_1) * conditional_probability_2

# Display Result
print(f"Conditional probability for next eruption < 60 mins: {combined_conditional_probability}")
