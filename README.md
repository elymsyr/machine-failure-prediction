# Machine Failure Prediction

This project involves creating a machine learning model to predict machine failure based on various features. The project is divided into several parts, including data visualization, model selection, model training, and creating a Tkinter-based application for real-time predictions.

## Project Overview

1. **Data Visualization and Feature Selection**: Analyzes the dataset to visualize relationships and select the most relevant features.
2. [**Model Selection with GridSearchCV**](https://www.kaggle.com/code/muhammadfaizan65/machine-failure-prediction-eda-modeling): Determines the best model and hyperparameters using GridSearchCV, from [Kaggle](https://www.kaggle.com/code/muhammadfaizan65/machine-failure-prediction-eda-modeling).
3. **Model Training**: Trains a Gradient Boosting model with the selected features and parameters.
4. **Tkinter Application**: Provides a graphical user interface (GUI) for real-time feature adjustments and predictions.

## Requirements

- Python 3.10.14
- Libraries: [requirements.txt](requirements.txt)

Install the required libraries using pip:

```bash
pip install -r requirements.txt
```

## [Data](https://www.kaggle.com/datasets/umerrtx/machine-failure-prediction-using-sensor-data)

### Overview
This dataset contains sensor data collected from various machines, intending to predict machine failures in advance. It includes a variety of sensor readings as well as recorded machine failures. Dataset has 944 row (1 repeated row.) and has no NaN values, from [Kaggle](https://www.kaggle.com/datasets/umerrtx/machine-failure-prediction-using-sensor-data)

### Features
 - footfall: The number of people or objects passing by the machine.
 - tempMode: The temperature mode or setting of the machine.
 - AQ: Air quality index near the machine.
 - USS: Ultrasonic sensor data, indicating proximity measurements.
 - CS: Current sensor readings, indicating the electrical current usage of the machine.
 - VOC: The level of volatile organic compounds detected near the machine.
 - RP: The machine parts' rotational position or RPM (revolutions per minute).
 - IP: Input pressure to the machine.
 - Temperature: The operating temperature of the machine.
 - fail: Binary indicator of machine failure (1 for failure, 0 for no failure).

#### Target Distribution

<img src="Images\failure_distribution.png" alt="failure_distribution" width="520"/>

## Results

### Results with [Data](Data\data.csv)
 - Features: `footfall`  `tempMode`  `AQ`  `USS`  `CS`  `VOC`  `RP`  `IP`  `Temperature`  `fail`
 - Test Size: 0.2
 - Data Size: 944
 - Results:
 ```
    Fitting 5 folds for each of 16 candidates, totalling 80 fits
    Best parameters for RandomForest: {'max_depth': None, 'n_estimators': 10}
    Accuracy for RandomForest: 0.8677248677248677
    Fitting 5 folds for each of 20 candidates, totalling 100 fits
    Best parameters for GradientBoosting: {'learning_rate': 0.1, 'n_estimators': 50}
    Accuracy for GradientBoosting: 0.8888888888888888
    Fitting 5 folds for each of 8 candidates, totalling 40 fits
    Best parameters for LogisticRegression: {'C': 0.01}
    Accuracy for LogisticRegression: 0.8783068783068783
    Fitting 5 folds for each of 16 candidates, totalling 80 fits
    Best parameters for SVM: {'C': 0.05, 'kernel': 'linear'}
    Accuracy for SVM: 0.873015873015873

    Best model: GradientBoosting with accuracy: 0.8888888888888888 
```

#### Feature Distribution

<img src="Images\feature_distribution.png" alt="failure_distribution" width="700"/>

#### Correlation Matrix

<img src="Images\correlation_matrix.png" alt="failure_distribution" width="600"/>

### Results with [Feature Reduced Data](Data\data_cleaned.csv)
 - Features: `AQ`  `USS`  `VOC` ` RP`  `IP`  `Temperature`  `fail`
 - Test Size: 0.2
 - Data Size: 944
 - Results:
 ```
    Fitting 5 folds for each of 16 candidates, totalling 80 fits
    Best parameters for RandomForest: {'max_depth': None, 'n_estimators': 50}
    Accuracy for RandomForest: 0.873015873015873
    Fitting 5 folds for each of 20 candidates, totalling 100 fits
    Best parameters for GradientBoosting: {'learning_rate': 0.05, 'n_estimators': 100}
    Accuracy for GradientBoosting: 0.8888888888888888
    Fitting 5 folds for each of 8 candidates, totalling 40 fits
    Best parameters for LogisticRegression: {'C': 0.01}
    Accuracy for LogisticRegression: 0.8783068783068783
    Fitting 5 folds for each of 16 candidates, totalling 80 fits
    Best parameters for SVM: {'C': 0.05, 'kernel': 'linear'}
    Accuracy for SVM: 0.873015873015873

    Best model: GradientBoosting with accuracy: 0.8888888888888888
```
#### Feature Distribution

<img src="Images\reduced_feature_distribution.png" alt="failure_distribution" width="700"/>

#### Correlation Matrix

<img src="Images\reduced_correlation_matrix.png" alt="failure_distribution" width="600"/>    