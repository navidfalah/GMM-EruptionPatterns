import pytest
from questions.question_b import compute_probability_with_pdf
from simulation import generate_dataset, calculate_probability_within_conditions


def test_probability_comparisons():
    computed_probability = compute_probability_with_pdf()

    # Generate test data for simulation comparison
    # Assuming generate_dataset() is a function that generates representative data
    test_data = generate_dataset()

    # Compute simulated probability based on actual data
    simulated_probability = calculate_probability_within_conditions(test_data)

    # Define a tolerance for comparison - this may need to be adjusted based on the expected variability
    tolerance = 0.05  # Example tolerance, adjust as needed

    # Compare the computed probability with the simulated one
    assert abs(computed_probability - simulated_probability) <= tolerance, "Computed probability does not match simulated probability within the defined tolerance."
