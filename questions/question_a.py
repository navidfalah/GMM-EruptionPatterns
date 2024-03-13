import sys
from os.path import dirname, join
sys.path.insert(0, join(dirname(__file__), '..'))
import logging
from questions.parameters import mix_ratio_1, mix_ratio_2
logging.basicConfig(level=logging.INFO, format='%(message)s')


def compute_expected_eruptions():
    expected_eruptions_1 = 10 * mix_ratio_1
    expected_eruptions_2 = 10 * mix_ratio_2
    return expected_eruptions_1, expected_eruptions_2

def display_and_log_expected_eruptions(expected_eruptions_1, expected_eruptions_2):
    result_msg_1 = f"Expected eruptions from component 1: {expected_eruptions_1:.3f}"
    result_msg_2 = f"Expected eruptions from component 2: {expected_eruptions_2:.3f}"
    logging.info(result_msg_1)
    logging.info(result_msg_2)

if __name__ == "__main__":
    expected_eruptions_1, expected_eruptions_2 = compute_expected_eruptions()
    display_and_log_expected_eruptions(expected_eruptions_1, expected_eruptions_2)
