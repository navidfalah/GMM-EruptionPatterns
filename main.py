from scipy.stats import multivariate_normal, norm
from scipy.stats import mvn

alpha1, alpha2 = 0.356, 0.644
mu1, mu2 = [2.04, 54.5], [4.29, 80.0]
sigma1 = [[0.0693, 0.436], [0.436, 33.7]]
sigma2 = [[0.170, 0.939], [0.939, 36.0]]

# a) 
expected_component_1 = 10 * alpha1
expected_component_2 = 10 * alpha2

# b)
lower_bound, upper_bound = [3, 60], [4, 70]
p1, _ = mvn.mvnun(lower_bound, upper_bound, mu1, sigma1)
p2, _ = mvn.mvnun(lower_bound, upper_bound, mu2, sigma2)
total_probability = alpha1 * p1 + alpha2 * p2

# c)
eruption_time_observed = 3
pdf_component1 = multivariate_normal(mu1, sigma1).pdf([eruption_time_observed, mu1[1]])
pdf_component2 = multivariate_normal(mu2, sigma2).pdf([eruption_time_observed, mu2[1]])
posterior1 = (pdf_component1 * alpha1) / (pdf_component1 * alpha1 + pdf_component2 * alpha2)

# d)
def conditional_probability(mu, sigma, rho, x2, target_x):
    conditional_mean = mu[0] + (rho * (sigma[0][1] / sigma[1][1]) * (x2 - mu[1]))
    conditional_variance = (1 - rho**2) * sigma[0][0]
    conditional_stddev = conditional_variance**0.5
    return norm.cdf(target_x, conditional_mean, conditional_stddev)

# Correlation coefficients (rho) for both components
rho1 = sigma1[0][1] / (sigma1[0][0]**0.5 * sigma1[1][1]**0.5)
rho2 = sigma2[0][1] / (sigma2[0][0]**0.5 * sigma2[1][1]**0.5)

# Calculate the conditional probabilities for both components
cond_prob1 = conditional_probability(mu1, sigma1, rho1, eruption_time_observed, 60)
cond_prob2 = conditional_probability(mu2, sigma2, rho2, eruption_time_observed, 60)

# Weighted conditional probabilities
final_conditional_probability = posterior1 * cond_prob1 + (1 - posterior1) * cond_prob2

# Output results
(expected_component_1, expected_component_2), total_probability, posterior1, final_conditional_probability
