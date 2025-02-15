# House Price Prediction App

Welcome to the House Price Prediction App! This application allows users to predict house prices based on various features such as area, number of bedrooms, number of bathrooms, neighbourhood, and year built. The predictions are made using three different models: Linear Regression, K-Nearest Neighbors (KNN), and Decision Tree.

## Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Models](#models)
- [Contributing](#contributing)
- [License](#license)

## Introduction
The House Price Prediction App is built using Python and Streamlit. It provides a user-friendly interface for predicting house prices based on input features. The app uses pre-trained models to generate predictions and displays the results.

## Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/puneeth-007/House_price_prediction.git
    ```
2. Navigate to the project directory:
    ```sh
    cd House_price_prediction
    ```
3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage
1. Run the app:
    ```sh
    streamlit run app.py
    ```
2. Open your web browser and go to the provided URL (usually `http://localhost:8501`).
3. Enter the features of the house in the input fields and click the "Predict" button to get the predictions.

## Features
- **Area (SquareFeet):** Enter the area of the house in square feet.
- **Bedrooms:** Enter the number of bedrooms in the house.
- **Bathrooms:** Enter the number of bathrooms in the house.
- **Neighbourhood:** Select the neighbourhood of the house (Rural, Suburb, Urban).
- **Year Built:** Enter the year the house was built.

## Models
The app uses three pre-trained models to predict house prices:
- **Linear Regression:** Provides the most accurate prediction.
- **K-Nearest Neighbors (KNN):** Predicts based on the average prices of the nearest neighbors.
- **Decision Tree:** Uses a tree-like model of decisions to predict the price.

