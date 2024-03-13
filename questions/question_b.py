import sys
from os.path import dirname, join, abspath
sys.path.insert(0, join(dirname(__file__), '..'))
import logging
from scipy.stats import multivariate_normal
from parameters import mix_ratio_1, mix_ratio_2, mean_1, mean_2, covariance_1, covariance_2
import numpy as np

sys.path.insert(0, join(dirname(__file__), '..'))
logging.basicConfig(level=logging.INFO, format='%(message)s')
import numpy as np
from scipy.stats import multivariate_normal
from scipy.integrate import dblquad
from parameters import mix_ratio_1, mix_ratio_2, mean_1, mean_2, covariance_1, covariance_2

def pdf_component(x, y, mean, covariance):
    """Calculate the PDF of a bivariate normal distribution for a given (x, y)."""
    rv = multivariate_normal(mean, covariance)
    return rv.pdf([x, y])

def integrate_pdf_over_range(mean, covariance, x_bounds, y_bounds):
    """Numerically integrate the PDF over a given rectangular range."""
    return dblquad(pdf_component, y_bounds[0], y_bounds[1], lambda x: x_bounds[0], lambda x: x_bounds[1], args=(mean, covariance))[0]

def compute_probability_with_pdf():
    x_bounds = [3, 4]  # Eruption duration between 3 and 4 minutes
    y_bounds = [60, 70]  # Time to next eruption between 60 and 70 minutes
    
    # Integrate over the PDF for each component
    probability_1 = integrate_pdf_over_range(mean_1, covariance_1, x_bounds, y_bounds)
    probability_2 = integrate_pdf_over_range(mean_2, covariance_2, x_bounds, y_bounds)
    
    # Weighted sum of probabilities for each component
    combined_probability = mix_ratio_1 * probability_1 + mix_ratio_2 * probability_2
    return combined_probability

if __name__ == "__main__":
    combined_probability = compute_probability_with_pdf()
    print(f"Probability of specified eruption durations using PDF integration: {combined_probability:.3f}")
