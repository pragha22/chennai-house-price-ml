# Chennai House Price Prediction (Machine Learning Project)

## Project Overview

This project builds a Machine Learning model to predict housing prices
in Chennai based on features such as area, number of bedrooms (BHK), and
location. The model is trained on a dataset of Chennai real estate
listings and deployed using a simple web application built with
Streamlit.

This project demonstrates the complete Machine Learning workflow: - Data
loading - Data preprocessing - Feature engineering - Model training -
Model evaluation - Model serialization - Web application deployment

The goal of this project is to showcase practical ML implementation
suitable for a portfolio or demonstration to recruiters.

------------------------------------------------------------------------

## Technologies Used

-   Python
-   Pandas
-   NumPy
-   Scikit-learn
-   Streamlit
-   Pickle

------------------------------------------------------------------------

## Project Structure

    chennai-house-price-ml/
    │
    ├── app.py                      # Streamlit web application
    ├── chennai_price_model.pkl     # Trained machine learning model
    ├── columns.pkl                 # Model feature columns
    ├── chennai-properties.csv      # Dataset used for training
    ├── requirements.txt            # Python dependencies
    └── README.md                   # Project documentation

------------------------------------------------------------------------

## Dataset

The dataset contains real estate listings from Chennai including:

-   Property location
-   Property size (square feet)
-   Number of bedrooms (BHK)
-   Price

The data is used to train a regression model that predicts housing
prices.

------------------------------------------------------------------------

## Machine Learning Workflow

### 1. Data Loading

The dataset is loaded using Pandas.

### 2. Data Cleaning

Missing values and unnecessary columns are removed.

### 3. Feature Engineering

Categorical variables such as location are converted into numerical
features using one-hot encoding.

### 4. Model Training

A Linear Regression model from Scikit-learn is used to train the
dataset.

### 5. Model Saving

The trained model and feature columns are saved using Pickle.

### 6. Deployment

A Streamlit web application allows users to input: - Area - Number of
bedrooms - Location

The app then predicts the house price.

------------------------------------------------------------------------

## Installation Instructions

Clone the repository:

    git clone https://github.com/pragha22/chennai-house-price-ml.git

Navigate to the project folder:

    cd chennai-house-price-ml

Install dependencies:

    pip install -r requirements.txt

------------------------------------------------------------------------

## Running the Application

Run the Streamlit application:

    streamlit run app.py

The application will open in your browser.

------------------------------------------------------------------------

## Example Usage

Input:

-   Area: 1200 sq ft
-   BHK: 2
-   Location: Tambaram

Output:

Estimated house price prediction.

------------------------------------------------------------------------

## Future Improvements

Possible enhancements:

-   Use advanced models such as Random Forest or Gradient Boosting
-   Add location dropdown instead of text input
-   Improve feature engineering
-   Deploy the application online
-   Add interactive visualizations

------------------------------------------------------------------------

## Deployment Options

This project can be deployed using:

-   Streamlit Community Cloud
-   Render
-   HuggingFace Spaces

These platforms allow recruiters to test the application directly from
the browser.

------------------------------------------------------------------------

## Author

Pragha

Machine Learning Enthusiast

------------------------------------------------------------------------

## License

This project is for educational and demonstration purposes.
