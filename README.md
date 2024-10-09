# Gold Price Prediction Model

This project predicts gold prices using a Random Forest Regressor. It also provides a simple web interface for visualization using **Streamlit**.

## Features

- **Data Analysis**: Provides an exploratory data analysis (EDA) including data description, missing value identification, and correlation matrix.
- **Prediction Model**: Implements a machine learning model to predict gold prices using a Random Forest Regressor.
- **Web App**: An interactive web interface for displaying predictions and model performance.

## Technologies Used

- **Python**
- **Numpy**
- **Pandas**
- **Matplotlib**
- **Seaborn**
- **Scikit-learn**
- **Streamlit**
- **PIL (Python Imaging Library)**

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your_username/gold-price-prediction.git
    cd gold-price-prediction
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows, use venv\Scripts\activate
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

## Dataset

The dataset used for this project contains gold price data. You can replace the `gold_price_data.csv` file with your dataset if needed.

## Usage

- The app allows you to visualize the dataset and check the model's performance.
- You can upload your dataset or modify the code to accommodate new features for gold price prediction.

## Model

The model used is a **Random Forest Regressor**, and the R2 score for model performance is calculated.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request.

## License

This project is licensed under the MIT License.
MIT License

Copyright (c) 2024 Fahith KRM

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

