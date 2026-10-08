import pandas as pd
import numpy as np
import os
import logging
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Configuration des logs du pipeline
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    logging.info("Initialisation du pipeline de données...")
    
    # 1. Ingestion des données (Dataset historique simulé pour le MVP)
    np.random.seed(42)
    n_samples = 1000

    data = {
        'Player': [f'Player_{i}' for i in range(n_samples)],
        'MIN': np.random.normal(20, 8, n_samples),
        'PTS': np.random.normal(10, 6, n_samples),
        'REB': np.random.normal(4, 3, n_samples),
        'AST': np.random.normal(2, 2, n_samples),
        'BLK': np.random.normal(0.5, 0.5, n_samples),
        'FG_PCT': np.random.normal(0.45, 0.05, n_samples)
    }
    df = pd.DataFrame(data)

    # 2. Feature Engineering & Labeling
    # Classification binaire : 1 (Profil All-Star), 0 (Role Player)
    df['All_Star'] = np.where((df['PTS'] > 15) & (df['MIN'] > 25), 1, 0)

    # 3. Préparation des datasets
    features = ['MIN', 'PTS', 'REB', 'AST', 'BLK', 'FG_PCT']
    X = df[features]
    y = df['All_Star']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # 4. Entraînement du modèle (Random Forest Classifier)
    logging.info("Entraînement du modèle Random Forest en cours...")
    model = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=42)
    model.fit(X_train, y_train)

    # 5. Évaluation des performances
    y_pred = model.predict(X_test)
    logging.info(f"Précision globale du modèle (Accuracy) : {accuracy_score(y_test, y_pred):.4f}")
    
    # 6. Sauvegarde de l'artefact
    os.makedirs('models', exist_ok=True)
    model_path = 'models/nba_rf_model.pkl'
    joblib.dump(model, model_path)
    logging.info(f"Artefact du modèle exporté avec succès vers : {model_path}")

if __name__ == "__main__":
    main()