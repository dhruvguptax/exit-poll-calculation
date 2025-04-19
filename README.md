
# Exit Poll Calculation Project

## Overview

The Exit Poll Calculation project uses machine learning to analyze exit poll data and predict election outcomes. The project includes data collection, preprocessing, model training, and prediction. It leverages the power of machine learning models to make predictions based on features like gender, age, and region.

The project consists of multiple components that allow users to:

- Train a predictive model using historical exit poll data.
- Make predictions on new exit poll data.
- Analyze the results through visualizations.

## Project Structure

```
exit-poll-calculation/
├── data/
│   ├── exit_poll_data.csv      # Raw exit poll data
│   ├── stratified_exit_poll_data.csv  # Stratified data for training
│   └── .gitkeep                # Keeps the folder in Git
├── model/
│   └── exit_poll_predictor.pkl # Pre-trained model for prediction
├── models/
│   ├── encoder.pkl             # Label encoder for categorical data
│   └── model.pkl               # Trained machine learning model
├── scripts/
│   ├── generate_data.py        # Script for generating stratified data
│   ├── predict.py              # Script for making predictions
│   ├── predictive_model.py     # Defines the model and training functions
│   ├── stratified_sampling.py  # Stratified sampling logic for data
│   ├── train_model.py          # Script to train the model
│   ├── visualization.py        # Script for visualizing results
│   └── .gitkeep                # Keeps the folder in Git
├── research.pdf                # Research paper explaining the project
├── main.py                     # Main script to run the project
├── pkl.py                      # Helper script for loading models
├── README.md                   # Project description
└── requirements.txt            # List of dependencies
```

## Setup and Installation

1. **Clone the repository:**

   Clone the repository to your local machine using:

   ```bash
   git clone https://github.com/dhruvguptax/exit-poll-calculation.git
   cd exit-poll-calculation
   ```

2. **Create a virtual environment:**

   It's recommended to use a virtual environment to manage dependencies:

   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment:**

   On Windows:
   
   ```bash
   venv\Scriptsctivate
   ```

   On Mac/Linux:
   
   ```bash
   source venv/bin/activate
   ```

4. **Install dependencies:**

   Install the necessary dependencies using:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Training the Model

To train the model using the provided data, run:

```bash
python scripts/train_model.py
```

This will train the machine learning model and save it along with the encoder in the `models/` directory.

### Making Predictions

To make predictions on new data, use the `predict.py` script:

```bash
python scripts/predict.py
```

You will need to provide new data in the same format as the original data.

### Visualizing Results

You can visualize the results of the exit poll predictions using the `visualization.py` script:

```bash
python scripts/visualization.py
```

This will generate visualizations of the model's performance and other key statistics.

## Files

- `research.pdf`: A detailed research paper explaining the methodology, reasoning, and steps taken in this project.
- `exit_poll_data.csv`: The raw data used for training the model.
- `stratified_exit_poll_data.csv`: The stratified version of the raw data used for more effective training.
- `exit_poll_predictor.pkl`: The trained machine learning model.
- `encoder.pkl`: The encoder used to process categorical features.

## Contributing

Contributions are welcome! If you have suggestions for improvements, feel free to fork the repository and submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
