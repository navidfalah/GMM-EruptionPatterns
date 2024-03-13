from questions.question_a import compute_expected_eruptions
from simulation import analyze_eruptions, generate_dataset
from questions.parameters import mix_ratio_1, mix_ratio_2

# Assuming your main module is named `eruption_analysis`, adjust imports as necessary
 # Adjust this import based on your actual module structure


def test_eruption_comparisons():
    # Mock the global parameters if they are external dependencies, else directly assign
    global mix_ratio_1, mix_ratio_2
    mix_ratio_1, mix_ratio_2 = 0.5, 0.5  # Example ratios, adjust as needed

    # Compute expected values using the main code
    expected_eruptions_1, expected_eruptions_2 = compute_expected_eruptions()

    # Generate test data for simulation/analytical comparison
    test_data = generate_dataset()

    # Compute simulated/analytical values
    # You will need to ensure analyze_eruptions and its dependencies are correctly implemented
    sim_eruptions_1, sim_eruptions_2 = analyze_eruptions(test_data)
    print(sim_eruptions_1)
    print(sim_eruptions_2)

    # Compare expected vs simulated/analytical values
    # You may want to use a tolerance for comparison due to the stochastic nature of simulations or analytical approximations
    tolerance = 0.1  # Adjust tolerance based on the expected precision of your simulation/analysis
    assert abs(expected_eruptions_1 - sim_eruptions_1/100) <= tolerance, "Component 1 eruption estimates do not match."
    assert abs(expected_eruptions_2 - sim_eruptions_2/100) <= tolerance, "Component 2 eruption estimates do not match."
