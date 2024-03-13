from scipy.stats import multivariate_normal
from parameters import (mix_ratio_1, mix_ratio_2,
mean_1, mean_2, covariance_1, covariance_2)
# Part B: Compute Probability of Specific Eruption Duration and Time Until Next Eruption

# GMM Parameters
bounds_start, bounds_end = [3, 60], [4, 70]

# Compute probability for each component
probability_1 = multivariate_normal(mean_1, covariance_1).cdf(bounds_end) - multivariate_normal(mean_1, covariance_1).cdf(bounds_start)
probability_2 = multivariate_normal(mean_2, covariance_2).cdf(bounds_end) - multivariate_normal(mean_2, covariance_2).cdf(bounds_start)
combined_probability = mix_ratio_1 * probability_1 + mix_ratio_2 * probability_2

# Display Result
print(f"Probability of specified eruption durations: {combined_probability}")
