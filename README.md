# Gold Price Prediction Model

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This project predicts gold prices using a Random Forest Regressor. It also provides a simple web interface for visualization using **Streamlit**.

## Features

- **Data Analysis**: Provides an exploratory data analysis (EDA) including data description, missing value identification, and correlation matrix.
- **Prediction Model**: Implements a machine learning model to predict gold prices using a Random Forest Regressor.
- **Web App**: An interactive web interface for displaying predictions and model performance.

## Technologies Used

- **Python** 
- **Numpy**: Numerical operations
- **Pandas**: Data manipulation and analysis
- **Matplotlib**: Plotting and visualization
- **Seaborn**: Statistical data visualization
- **Scikit-learn**: Machine learning algorithms (RandomForestRegressor, train_test_split, r2_score)
- **Streamlit**: Web app framework
- **PIL (Python Imaging Library)**Pillow: Image handling in Streamlit for loading images


## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your_username/gold-price-prediction.git
    ```
    ```bash
    cd gold-price-prediction
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    ```
    ```bash
    # On macOS/Linux :
    source venv/bin/activate
    ```
    ```bash
     # On Windows : 
    venv\Scripts\activate
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
    ![WhatsApp Image 2024-10-10 at 01 02 27_fd3385eb](https://github.com/user-attachments/assets/62efd050-1524-4661-89be-70d9579d0c8e)


4. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

    ![WhatsApp Image 2024-10-10 at 01 02 04_c181d1d2](https://github.com/user-attachments/assets/dccd421f-761b-4a0f-b7c6-d7680e1ed5eb)


## Dataset

The dataset used for this project contains gold price data. You can replace the `gold_price_data.csv` file with your dataset if needed.
Dataset Link : https://www.kaggle.com/datasets/altruistdelhite04/gold-price-data

## Usage

- The app allows you to visualize the dataset and check the model's performance.
- You can upload your dataset or modify the code to accommodate new features for gold price prediction.

## Model

The model used is a **Random Forest Regressor**, and the R2 score for model performance is calculated.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
