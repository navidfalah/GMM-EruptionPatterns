from parameters import mix_ratio_1, mix_ratio_2
# Part A: Expected Number of Eruptions from Each Component

# Compute expected number of eruptions for each component from 10 total eruptions
expected_eruptions_1 = 10 * mix_ratio_1
expected_eruptions_2 = 10 * mix_ratio_2

# Display Results

if __name__ == "__main__":
    print(f"Expected eruptions from component 1: {expected_eruptions_1:.3f}")
    print(f"Expected eruptions from component 2: {expected_eruptions_2:.3f}")
