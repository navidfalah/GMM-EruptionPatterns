from scipy.stats import multivariate_normal
from parameters import mix_ratio_1, mix_ratio_2, mean_1, mean_2, covariance_1, covariance_2
import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')

# GMM Parameters
bounds_start, bounds_end = [3, 60], [4, 70]

# Compute probability for each component
probability_1 = multivariate_normal(mean_1, covariance_1).cdf(bounds_end) - multivariate_normal(mean_1, covariance_1).cdf(bounds_start)
probability_2 = multivariate_normal(mean_2, covariance_2).cdf(bounds_end) - multivariate_normal(mean_2, covariance_2).cdf(bounds_start)
combined_probability = mix_ratio_1 * probability_1 + mix_ratio_2 * probability_2

# Display and log Result
if __name__ == "__main__":
    result_msg = f"Probability of specified eruption durations: {combined_probability:.3f}"
    logging.info(result_msg)
