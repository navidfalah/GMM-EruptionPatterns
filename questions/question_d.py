import sys
from os.path import dirname, join, abspath
sys.path.insert(0, join(dirname(__file__), '..'))
import logging
from scipy.stats import norm
from parameters import mean_1, mean_2, covariance_1, covariance_2

logging.basicConfig(level=logging.INFO, format='%(message)s')

def compute_conditional_probability(observed_eruption_time, updated_probability_1):
    conditional_mean_1 = mean_1[1] + (covariance_1[0][1] / covariance_1[0][0]**0.5) * (observed_eruption_time - mean_1[0])
    conditional_variance_1 = covariance_1[1][1] * (1 - (covariance_1[0][1]**2 / (covariance_1[0][0] * covariance_1[1][1])))
    conditional_probability_1 = norm(conditional_mean_1, conditional_variance_1**0.5).cdf(60)

    conditional_mean_2 = mean_2[1] + (covariance_2[0][1] / covariance_2[0][0]**0.5) * (observed_eruption_time - mean_2[0])
    conditional_variance_2 = covariance_2[1][1] * (1 - (covariance_2[0][1]**2 / (covariance_2[0][0] * covariance_2[1][1])))
    conditional_probability_2 = norm(conditional_mean_2, conditional_variance_2**0.5).cdf(60)

    combined_conditional_probability = updated_probability_1 * conditional_probability_1 + (1 - updated_probability_1) * conditional_probability_2
    return combined_conditional_probability

if __name__ == "__main__":
    observed_eruption_time = 3
    updated_probability_1 = 0.130  # Assuming this value is derived from part C
    conditional_probability = compute_conditional_probability(observed_eruption_time, updated_probability_1)
    result_msg = f"Conditional probability for next eruption < 60 mins: {conditional_probability:.3f}"
    logging.info(result_msg)
