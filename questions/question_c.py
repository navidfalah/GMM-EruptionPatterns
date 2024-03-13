import sys
from os.path import dirname, join, abspath
sys.path.insert(0, join(dirname(__file__), '..'))
from scipy.stats import norm
from parameters import mix_ratio_1, mix_ratio_2, mean_1, mean_2, covariance_1, covariance_2
import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')

# Observed data
observed_eruption_time = 3  # Observed eruption time in minutes

# Calculate the likelihood of the observed eruption time under each component
likelihood_1 = norm(mean_1[0], covariance_1[0][0]**0.5).pdf(observed_eruption_time)
likelihood_2 = norm(mean_2[0], covariance_2[0][0]**0.5).pdf(observed_eruption_time)

# Update the probability for component 1 using Bayes' Theorem
updated_probability_1 = (likelihood_1 * mix_ratio_1) / ((likelihood_1 * mix_ratio_1) + (likelihood_2 * mix_ratio_2))

# Display and log the updated probability for component 1
if __name__ == "__main__":
    result_msg = f"Updated probability for component 1: {updated_probability_1:.3f}"
    logging.info(result_msg)
