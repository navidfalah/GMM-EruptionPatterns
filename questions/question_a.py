from parameters import mix_ratio_1, mix_ratio_2
import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')

# Compute expected number of eruptions for each component from 10 total eruptions
expected_eruptions_1 = 10 * mix_ratio_1
expected_eruptions_2 = 10 * mix_ratio_2

# Display and log Results
if __name__ == "__main__":
    result_msg_1 = f"Expected eruptions from component 1: {expected_eruptions_1:.3f}"
    result_msg_2 = f"Expected eruptions from component 2: {expected_eruptions_2:.3f}"
    logging.info(result_msg_1)
    logging.info(result_msg_2)
