# 🏀 Prédicteur de Potentiel All-Star NBA

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Machine_Learning-orange.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-Interactive_App-red.svg)

## 📌 Présentation du projet
L'objectif de cette application est de prédire si un jeune joueur de la NBA (Rookie) a le profil statistique pour devenir un futur "All-Star" au cours de sa carrière. 

Plutôt que de se limiter à la simple lecture d'un tableau de statistiques, j'ai voulu créer un outil interactif basé sur le Machine Learning. L'application analyse les performances d'un joueur lors de sa première année et calcule instantanément sa probabilité de réussite. Cela permet de mieux comprendre de manière concrète quels sont les facteurs qui déterminent le succès d'un rookie dans la ligue.

🌐 **[Tester l'application en direct ici](https://nba-prospect-analytics-ncuqf6edufs4kms22xxhl3.streamlit.app/)**

## 🛠️ Outils et Technologies utilisés
Pour construire ce projet de A à Z, je me suis appuyé sur l'écosystème Python orienté Data Science :
- **Pandas et NumPy :** pour la manipulation, le nettoyage et la structuration des données statistiques historiques.
- **Scikit-Learn :** pour la phase de Machine Learning, notamment la création et l'entraînement d'un modèle de classification de type *Random Forest*.
- **Streamlit :** pour le développement de l'interface web interactive, permettant de rendre le modèle utilisable sans aucune ligne de commande.
- **Matplotlib :** pour la génération des graphiques d'analyse.

## 📊 Fonctionnalités de l'application
1. **Saisie interactive :** L'utilisateur peut modifier manuellement les statistiques clés d'un joueur (Minutes jouées, Points, Rebonds, Passes, Contres, Efficacité au tir) à l'aide de curseurs.
2. **Prédiction en temps réel :** Le modèle Random Forest calcule directement la probabilité (en pourcentage) que le joueur atteigne un statut majeur.
3. **Explicabilité du modèle :** Au lieu de donner un simple chiffre, l'application génère un rapport écrit qui explique *pourquoi* le joueur a obtenu ce score, en listant ses points forts et les seuils statistiques à améliorer.
4. **Poids des variables :** Un graphique montre de façon transparente quelles sont les statistiques que l'algorithme juge les plus importantes.

## 🚀 Comment lancer le projet chez vous

Si vous souhaitez explorer le code et faire tourner l'application sur votre propre machine :

1. Clonez ce dépôt localement :
   ```bash
   git clone [https://github.com/thomas-aymard/nba-prospect-analytics.git](https://github.com/thomas-aymard/nba-prospect-analytics.git)
   cd nba-prospect-analytics
