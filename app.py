import pandas as pd
import numpy as np

# Charger les données depuis un fichier CSV
df = pd.read_csv('data.csv')

# Supprimer les lignes ayant des valeurs manquantes
df.dropna(inplace=True)

# Supprimer les colonnes inutiles
df.drop(['id', 'date', 'url'], axis=1, inplace=True)

# Convertir la colonne "price" en float
df['price'] = df['price'].astype(float)

# Encoder les variables catégorielles en utilisant One-Hot Encoding
df = pd.get_dummies(df, columns=['category', 'location'], drop_first=True)

# Normaliser les données numériques
numeric_cols = ['price', 'bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'floors']
df[numeric_cols] = (df[numeric_cols] - df[numeric_cols].mean()) / df[numeric_cols].std()

# Diviser les données en ensembles d'entraînement et de test
train_data = df.sample(frac=0.8, random_state=1)
test_data = df.drop(train_data.index)

# Séparer les étiquettes des données d'entraînement et de test
X_train = train_data.drop('price', axis=1)
y_train = train_data['price']

X_test = test_data.drop('price', axis=1)
y_test = test_data['price']

#J'ai chargé des données à partir d'un fichier CSV, supprimé les lignes ayant des valeurs manquantes, supprimé les colonnes inutiles, converti la colonne "price" en
#float, encodé les variables catégorielles en utilisant One-Hot Encoding, normalisé les données numériques et divisé les données en ensembles d'entraînement et de test.

Ce prétraitement des données est une étape importante dans la plupart des projets de science des données, car il permet de préparer les données pour l'entraînement et l'évaluation des modèles.
