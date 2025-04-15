# src/train.py

import pandas as pd
import numpy as np
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import f1_score, roc_auc_score, accuracy_score
from sklearn.ensemble import RandomForestClassifier

from imblearn.over_sampling import SMOTE

def preparar_dados(df):
    df_temp = df.copy()
    le = LabelEncoder()
    df_temp['sexo'] = le.fit_transform(df_temp['sexo'])
    df_temp = pd.get_dummies(df_temp, columns=['assinatura', 'duracao_contrato'], drop_first=True)
    X = df_temp.drop(['cancelou', 'CustomerID'], axis=1)
    y = df_temp['cancelou']
    return X, y

def balancear(X, y):
    sm = SMOTE(random_state=42)
    return sm.fit_resample(X, y)

def treinar_modelo(X_train, y_train):
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)
    return model

def avaliar(model, X_test, y_test):
    y_pred = model.predict(X_test)
    y_proba = model.predict_proba(X_test)[:,1]
    print("Acurácia:", accuracy_score(y_test, y_pred))
    print("F1-score:", f1_score(y_test, y_pred))
    print("ROC AUC:", roc_auc_score(y_test, y_proba))

def main():
    df = pd.read_csv("cancelamentos.csv").dropna()
    X, y = preparar_dados(df)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, stratify=y, random_state=42)
    X_train_res, y_train_res = balancear(X_train, y_train)
    modelo = treinar_modelo(X_train_res, y_train_res)
    avaliar(modelo, X_test, y_test)
    joblib.dump(modelo, "outputs/models/modelo_rf.pkl")

if __name__ == "__main__":
    main()
