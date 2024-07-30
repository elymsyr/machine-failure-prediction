# Machine Failure Prediction

This project involves creating a machine learning model to predict machine failure based on various features. The project is divided into several parts, including data visualization, model selection, model training, and creating a Tkinter-based application for real-time predictions.

 - [Data Link](https://www.kaggle.com/datasets/umerrtx/machine-failure-prediction-using-sensor-data)
 - [Model Selection with GridSearchCV Link](https://www.kaggle.com/code/muhammadfaizan65/machine-failure-prediction-eda-modeling)

## Project Overview

1. **Data Visualization and Feature Selection**: Analyzes the dataset to visualize relationships and select the most relevant features.
2. **Model Selection with GridSearchCV**: Determines the best model and hyperparameters using GridSearchCV.
3. **Model Training**: Trains a Gradient Boosting model with the selected features and parameters.
4. **Tkinter Application**: Provides a graphical user interface (GUI) for real-time feature adjustments and predictions.

## Requirements

- Python 3.10.14
- Libraries: [requirements.txt](requirements.txt)

Install the required libraries using pip:

```bash
pip install -r requirements.txt
```

## Data

### Overview
This dataset contains sensor data collected from various machines, with the aim of predicting machine failures in advance. It includes a variety of sensor readings as well as the recorded machine failures.

### Features
 - footfall     944 non-null    int64: The number of people or objects passing by the machine.
 - tempMode     944 non-null    int64: The temperature mode or setting of the machine.
 - AQ           944 non-null    int64: Air quality index near the machine.
 - USS          944 non-null    int64: Ultrasonic sensor data, indicating proximity measurements.
 - CS           944 non-null    int64: Current sensor readings, indicating the electrical current usage of the machine.
 - VOC          944 non-null    int64: Volatile organic compounds level detected near the machine.
 - RP           944 non-null    int64: Rotational position or RPM (revolutions per minute) of the machine parts.
 - IP           944 non-null    int64: Input pressure to the machine.
 - Temperature  944 non-null    int64: The operating temperature of the machine.
 - fail         944 non-null    int64: Binary indicator of machine failure (1 for failure, 0 for no failure).


## Results

### Results with [Data](Data\data.csv)
 - Features : `footfall`,`tempMode`,`AQ`,`USS`,`CS`,`VOC`,`RP`,`IP`,`Temperature`,`fail`
 - Test Size : 0.2
 - Data Size: 944 
 - Results:
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

### Results with [Feature Reduced Data](Data\data_cleaned.csv)
 - Features: `AQ`,`USS`,`VOC`,`RP`,`IP`,`Temperature`,`fail`
 - Test Size: 0.2
 - Data Size: 944
 - Results:
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