from questions.question_a import compute_expected_eruptions
from questions.question_b import compute_probability_with_pdf
from questions.question_c import calculate_likelihood, update_probability
from questions.question_d import compute_conditional_probability
from simulation import (simulate_conditional_distribution,
analyze_eruptions, generate_dataset, calculate_updated_probability,
generate_dataset, calculate_probability_within_conditions)


def test_eruption_comparisons():
    expected_eruptions_1, expected_eruptions_2 = compute_expected_eruptions()
    test_data = generate_dataset()
    sim_eruptions_1, sim_eruptions_2 = analyze_eruptions(test_data)
    tolerance = 0.1
    assert abs(expected_eruptions_1 - sim_eruptions_1/100) <= tolerance, "Component 1 eruption estimates do not match."
    assert abs(expected_eruptions_2 - sim_eruptions_2/100) <= tolerance, "Component 2 eruption estimates do not match."

def test_probability_comparisons():
    computed_probability = compute_probability_with_pdf()
    test_data = generate_dataset()
    simulated_probability = calculate_probability_within_conditions(test_data)
    tolerance = 0.05
    assert abs(computed_probability - simulated_probability) <= tolerance, "Computed probability does not match simulated probability within the defined tolerance."

def test_updated_probability():
    observed_eruption_time = 3
    likelihood_1, likelihood_2 = calculate_likelihood(observed_eruption_time)
    updated_prob_1 = update_probability(likelihood_1, likelihood_2)
    expected_updated_prob_1 = calculate_updated_probability(observed_eruption_time)
    tolerance = 0.01
    assert abs(updated_prob_1 - expected_updated_prob_1) <= tolerance, "Updated probability does not match expected probability within the defined tolerance."

def test_conditional_probability():
    observed_eruption_time = 3
    updated_probability_1 = 0.130
    analytical_conditional_prob = compute_conditional_probability(observed_eruption_time, updated_probability_1)
    simulated_conditional_prob = simulate_conditional_distribution(num_samples=500, observed_eruption_time=observed_eruption_time, updated_probability_1=updated_probability_1)
    tolerance = 0.05
    assert abs(analytical_conditional_prob - simulated_conditional_prob) <= tolerance, "Analytical conditional probability does not match simulated conditional probability within the defined tolerance."
