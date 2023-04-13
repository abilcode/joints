from sklearn.model_selection import StratifiedKFold, KFold
from sklearn.metrics import f1_score
import pandas as pd 

def cross_validation(X,y,model):
    skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
    for train_index, test_index in skf.split(X, y):
        X_train, X_test = X.iloc[train_index], X.iloc[test_index]
        y_train, y_test = y.iloc[train_index], y.iloc[test_index]
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        f1_macro = f1_score(y_test, y_pred, average = 'macro')
    return f1_macro