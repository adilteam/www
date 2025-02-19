# Umico.az Data Analyse and Modeling

```bash
C:.
├───.idea
│   └───inspectionProfiles
├───.ipynb_checkpoints
├───data_mining
│   ├───.idea
│   │   └───inspectionProfiles
│   └───umico_az
│       ├───spiders
│       │   └───__pycache__
│       └───__pycache__
└───modelling
    └───.ipynb_checkpoints
```
## Table of Contents

- [Overview](#overview)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)
- [Modeling](#modeling)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)

## Overview

This project is an in-depth data analysis and modeling effort conducted on the Umico.az dataset. Umico.az is a popular online marketplace where various products are offered with discounts. The project aims to explore, understand, and model the data to gain insights into product discounts, pricing, sellers, and more.

## Project Structure

The project directory structure is organized as follows:

- **data_mining**: Contains web scraping code using Scrapy.
  - **umico_az**: Scrapy project folder.
    - **spiders**: Scrapy spider scripts.

- **modelling**: Contains Jupyter Notebook files for data analysis and modeling.

## Getting Started

To run the data analysis and modeling tasks, you will need Python and the following libraries installed:

- pandas
- matplotlib
- seaborn
- scikit-learn
- xgboost

You can install these libraries using pip:

```bash
pip install pandas matplotlib seaborn scikit-learn xgboost
```

## Exploratory Data Analysis (EDA)

Exploratory Data Analysis (EDA) is performed to understand the dataset and draw insights. The EDA tasks include:

- Data loading and summary statistics.
- Visualizations of discount percentages, real prices, and more.
- Analysis of sellers, titles, and their market shares.

## Modeling

Two regression models are implemented:

1. **Linear Regression**: A basic linear regression model is built to predict discount percentages based on various features.

2. **XGBoost Regression**: A more advanced XGBoost regression model is created to predict discount percentages with improved performance.

Feature importance is visualized for the XGBoost model.

## Results

The project provides valuable insights into product discounts, seller performance, and the effectiveness of regression models in predicting discount percentages. You can find detailed analysis and model performance metrics in the Jupyter Notebook files.

## Contributing

Contributions to this project are welcome. If you would like to contribute, please follow these guidelines:

- Fork the repository.
- Create a new branch for your feature or fix.
- Make your changes and submit a pull request.
