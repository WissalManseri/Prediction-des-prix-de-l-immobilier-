# Projet de prédiction des prix immobiliers
# Objectif
L'objectif de ce projet est de créer un modèle de prédiction des prix immobiliers à partir de données d'annonces immobilières. Nous allons utiliser une base de données de ventes de maisons pour entraîner notre modèle et tester sa performance sur une base de données de test.

Ce code utilise des techniques de préparation des données pour nettoyer et normaliser un ensemble de données immobilières, et entraîne un modèle de régression linéaire pour prédire les prix de l'immobilier.


<img src="https://user-images.githubusercontent.com/89531771/225853423-3d406788-c9d5-4040-8c5d-b92ecdf6641d.jpg" width="1000" height="500">


#Installation
Pour exécuter ce code, vous aurez besoin de Python 3 et des bibliothèques suivantes : pandas, numpy, et scikit-learn. Vous pouvez les installer en utilisant la commande suivante :

    pip install pandas numpy scikit-learn

# Données
 Le fichier CSV contient des informations sur les ventes de maisons, y compris le prix de vente, la surface habitable, le nombre de chambres, le nombre de salles de bains, le quartier, etc.

# Prétraitement des données
Avant de pouvoir entraîner notre modèle, nous devons prétraiter les données. 

Les étapes de prétraitement comprennent :

1. Supprimer les lignes ayant des valeurs manquantes
2. Supprimer les colonnes inutiles
3. Convertir la colonne "price" en float
4. Encoder les variables catégorielles en utilisant One-Hot Encoding
5. Normaliser les données numériques
6. Entraînement du modèle
8. J'ai divisé les données en ensembles d'entraînement et de test. Le modèle a été entraîné sur l'ensemble d'entraînement et testé sur l'ensemble de test.
9. J'ai également évalué la performance du modèle en utilisant des métriques telles que le RMSE (Root Mean Squared Error) et le R2 Score.

# Comment utiliser ce code

Pour exécuter ce code sur vos propres données, vous devrez suivre les étapes suivantes :

1. Télécharger le fichier de données CSV et le placer dans le même dossier que le script Python.
2. Installer les bibliothèques Python nécessaires (pandas, numpy, scikit-learn).
3. Ouvrir le script Python dans un éditeur de texte et changer le nom du fichier CSV si nécessaire.
4. Exécuter le script Python.  
5.avec la commande suivante :

        python predict_housing_prices.py
        
Le script chargera les données à partir du fichier CSV, effectuera la préparation des données, entraînera le modèle de régression linéaire, et affichera l'accuracy du modèle sur les données de test.


# Auteur
Ce projet a été réalisé par WISSAL MANSRI.

N'hésitez pas à me contacter si vous avez des questions ou des commentaires sur ce projet.






