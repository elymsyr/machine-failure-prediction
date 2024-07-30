import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier

def data_split(path: str = 'Data/data_cleaned.csv', target_column: str = 'fail', test_size: float = 0.2, random_state: int = 42):
    data = pd.read_csv("..\Data\data.csv")
    # Data Preprocessing
    X = data.drop(columns=[target_column])
    y = data[target_column]
    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)    
    # Standardize the features
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)
    return data, X_train, X_test, y_train, y_test, scaler, X, y

def model_train_random_forest(X_train, y_train, max_depth=20, n_estimators=100):
    model = RandomForestClassifier(max_depth=max_depth, n_estimators=n_estimators)
    model.fit(X_train, y_train)
    return model

def model_train_gradient(X_train, y_train, learning_rate=0.1, n_estimators=50): # GradientBoosting: {'learning_rate': 0.1, 'n_estimators': 50}
    model = GradientBoostingClassifier(learning_rate=learning_rate, n_estimators=n_estimators)
    model.fit(X_train, y_train)
    return model

def predict_new_row(new_row: np.array, scaler: StandardScaler, model: RandomForestClassifier):
    new_row_scaled = scaler.transform(new_row)
    probability = model.predict_proba(new_row_scaled)[0, 1]
    return probability