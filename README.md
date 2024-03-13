# Old Faithful Eruption Analysis Repository 🌋

Explore the fascinating eruption patterns of Old Faithful geyser in Yellowstone National Park. The repository delves into analyzing the duration of eruptions and the intervals between them, which are modeled using a sophisticated 2-component Gaussian mixture model (GMM). Discover insights into the predictability and behavior of this iconic natural phenomenon. 🏞️

## Getting Started 🚀

To embark on this volcanic journey:

1. **Clone the Project** 📥
   ```
   git clone https://github.com/navidfalah/GMM-EruptionPatterns.git
   ```

2. **Navigate to the Project Directory** 📂
   ```
   cd GMM-EruptionPatterns
   ```

3. **Create a Virtual Environment** 🐍
   ```
   python -m venv .venv
   ```

4. **Activate the Virtual Environment** 💻
   - For Windows:
     ```
     .venv\Scripts\activate
     ```
   - For Unix/macOS:
     ```
     source .venv/bin/activate
     ```

5. **Install Dependencies** 🛠️
   ```
   pip install -r requirements.txt
   ```

6. **Set PYTHONPATH Environment Variable** 🌐
   ```
   export PYTHONPATH=/home/navid/Desktop/GMM-EruptionPatterns
   ```

Now you're all set to explore the volcanic eruption analysis project! 🌋

## Project Overview 📋

Explore the key components of the project:

- **main.py**: Executes the answers to the questions located in the `questions` directory using subprocess.
- **simulation.py**: Provides a simulated conditional distribution and delivers data in an alternative format.
- **tests/test_questions.py**: Contains unit tests to verify the functionalities of the functions located in the `questions` module using pytest.

## Actual Data 📊

![Actual Data](https://raw.githubusercontent.com/navidfalah/GMM-EruptionPatterns/main/data/actual.png)

The actual data represents the eruption patterns observed at Old Faithful geyser in Yellowstone National Park. It follows a 2-component Gaussian mixture model (GMM) where each component represents a distinct pattern of eruption behavior.

A 2-component GMM with full covariance matrices was fitted to the data using the Expectation-Maximization (EM) algorithm. The estimated parameters are as follows:
- Component Prior Probabilities: α̂₁ = 0.356, α̂₂ = 0.644.
- Component Means: 𝜇̂₁ = [2.04, 54.5], 𝜇̂₂ = [4.29, 80.0].
- Component Covariance Matrices:
  𝚺̂₁ = [[0.0693, 0.436],
         [0.436, 33.7]],
  𝚺̂₂ = [[0.170, 0.939],
         [0.939, 36.0]].

## Simulated Data 📈

![Simulated Data](https://raw.githubusercontent.com/navidfalah/GMM-EruptionPatterns/main/data/simulated.png)

The simulated data represents the eruption patterns generated using the parameters estimated from the actual data. It helps verify the accuracy of the GMM model in capturing the underlying eruption behavior.

## Usage 🧑‍💻

### Running the Project 🚀

To get the answer of the questions:

```
python main.py
```

### Running the Simulation 🌐

To witness the eruption analysis in action:

```
python simulation.py
```

Marvel at the results as they unfold before your eyes! 🤩

### Running Unit Tests 🧪

For peace of mind and confidence in our analysis:

```
pytest
```

Witness the tests ensuring the integrity of our eruption analysis functions! 🔍

## Project Structure 🌳

```

├── LICENSE
├── main.py
├── questions
│   ├── __init__.py
│   ├── parameters.py
│   ├── question_a.py
│   ├── question_b.py
│   ├── question_c.py
│   └── question_d.py
├── README.md
├── requirements.txt
├── script_logs.log
├── simulation.py
└── tests
    ├── __init__.py
    └── test_qusetions.py

```

## Contributors 👥

## License ⚖️

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.