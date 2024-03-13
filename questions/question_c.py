import sys
from os.path import dirname, join, abspath
sys.path.insert(0, join(dirname(__file__), '..'))
import logging
from scipy.stats import norm
from parameters import mix_ratio_1, mix_ratio_2, mean_1, mean_2, covariance_1, covariance_2

logging.basicConfig(level=logging.INFO, format='%(message)s')

def calculate_likelihood(observed_eruption_time):
    likelihood_1 = norm(mean_1[0], covariance_1[0][0]**0.5).pdf(observed_eruption_time)
    likelihood_2 = norm(mean_2[0], covariance_2[0][0]**0.5).pdf(observed_eruption_time)
    return likelihood_1, likelihood_2

def update_probability(likelihood_1, likelihood_2):
    updated_probability_1 = (likelihood_1 * mix_ratio_1) / ((likelihood_1 * mix_ratio_1) + (likelihood_2 * mix_ratio_2))
    return updated_probability_1

if __name__ == "__main__":
    observed_eruption_time = 3
    likelihood_1, likelihood_2 = calculate_likelihood(observed_eruption_time)
    updated_probability_1 = update_probability(likelihood_1, likelihood_2)
    result_msg = f"Updated probability for component 1: {updated_probability_1:.3f}"
    logging.info(result_msg)
