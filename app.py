import streamlit as st
import pandas as pd
import joblib

# Configuration de la page
st.set_page_config(page_title="NBA Prospect Analytics", page_icon="🏀", layout="centered")

# --- GESTION DE LA LANGUE (BILINGUE) ---
if 'lang' not in st.session_state:
    st.session_state['lang'] = 'FR'

# Sélecteur de langue dans la barre latérale
lang_choice = st.sidebar.radio("🌐 Language / Langue", ['FR', 'EN'], horizontal=True)
st.session_state['lang'] = lang_choice
lang = st.session_state['lang']

# Dictionnaires de traduction pour l'interface statique
ui = {
    'FR': {
        'title': "🏀 NBA Prospect Analytics Engine",
        'subtitle': "**Advanced Scouting & Performance Projection**\n\nOutil décisionnel prédictif évaluant le potentiel de développement d'un prospect NBA sur la base de ses métriques de saison Rookie.",
        'error_model': "⚠️ Artefact du modèle introuvable. Veuillez exécuter le pipeline de données (`train_model.py`) au préalable.",
        'sb_header': "Paramètres du Prospect",
        'sb_player': "Identifiant Joueur",
        'sb_metrics': "Métriques (Moyennes par match)",
        'btn_predict': "📊 Générer le Rapport de Projection",
        'res_title': "Rapport de Performance :",
        'kpi_prob': "Projection Statut All-Star",
        'tier_high': "✅ Tier projeté : Franchise Player / All-Star",
        'tier_low': "⚠️ Tier projeté : Role Player / Rotation",
        'exec_sum': "### 📋 Executive Summary",
        'feat_title': "### 🔍 Feature Importance",
        'feat_desc': "Distribution de l'impact des différentes métriques dans le processus de classification du système de Machine Learning.",
        'metric_col': "Métrique"
    },
    'EN': {
        'title': "🏀 NBA Prospect Analytics Engine",
        'subtitle': "**Advanced Scouting & Performance Projection**\n\nPredictive decision tool evaluating an NBA prospect's developmental potential based on their Rookie season metrics.",
        'error_model': "⚠️ Model artifact not found. Please run the data pipeline (`train_model.py`) first.",
        'sb_header': "Prospect Parameters",
        'sb_player': "Player ID",
        'sb_metrics': "Metrics (Per Game Averages)",
        'btn_predict': "📊 Generate Projection Report",
        'res_title': "Performance Report:",
        'kpi_prob': "All-Star Status Projection",
        'tier_high': "✅ Projected Tier: Franchise Player / All-Star",
        'tier_low': "⚠️ Projected Tier: Role Player / Rotation",
        'exec_sum': "### 📋 Executive Summary",
        'feat_title': "### 🔍 Feature Importance",
        'feat_desc': "Impact distribution of various metrics within the Machine Learning system's classification process.",
        'metric_col': "Metric"
    }
}

# En-tête du Dashboard
st.title(ui[lang]['title'])
st.write(ui[lang]['subtitle'])

# Chargement de l'artefact du modèle
@st.cache_resource
def load_model():
    try:
        return joblib.load('models/nba_rf_model.pkl')
    except FileNotFoundError:
        return None

model = load_model()

if model is None:
    st.error(ui[lang]['error_model'])
else:
    # --- BARRE LATÉRALE ---
    st.sidebar.header(ui[lang]['sb_header'])
    player_name = st.sidebar.text_input(ui[lang]['sb_player'], "Victor Wembanyama")
    
    st.sidebar.subheader(ui[lang]['sb_metrics'])
    # Les labels des sliders s'adaptent selon la langue
    min_label = "Minutes (MIN)" if lang == 'FR' else "Minutes Played (MIN)"
    pts_label = "Points (PTS)" if lang == 'FR' else "Points (PTS)"
    reb_label = "Rebonds (REB)" if lang == 'FR' else "Rebounds (REB)"
    ast_label = "Passes (AST)" if lang == 'FR' else "Assists (AST)"
    blk_label = "Contres (BLK)" if lang == 'FR' else "Blocks (BLK)"
    fg_pct_label = "Efficacité (FG%)" if lang == 'FR' else "Field Goal (FG%)"

    min_played = st.sidebar.slider(min_label, 5.0, 40.0, 29.7)
    pts = st.sidebar.slider(pts_label, 0.0, 35.0, 21.4)
    reb = st.sidebar.slider(reb_label, 0.0, 15.0, 10.6)
    ast = st.sidebar.slider(ast_label, 0.0, 15.0, 3.9)
    blk = st.sidebar.slider(blk_label, 0.0, 5.0, 3.6)
    fg_pct = st.sidebar.slider(fg_pct_label, 0.300, 0.700, 0.465)

    st.sidebar.markdown("---")
    st.sidebar.markdown("👨‍💻 **Lead Data Scientist:** Thomas AYMARD")

    # Formatage des données d'entrée
    input_data = pd.DataFrame({
        'MIN': [min_played],
        'PTS': [pts],
        'REB': [reb],
        'AST': [ast],
        'BLK': [blk],
        'FG_PCT': [fg_pct]
    })

    if st.button(ui[lang]['btn_predict']):
        # Inférence
        probability = model.predict_proba(input_data)[0][1]

        st.subheader(f"{ui[lang]['res_title']} {player_name}")
        
        # KPIs Principaux
        col1, col2 = st.columns(2)
        with col1:
            st.metric(ui[lang]['kpi_prob'], f"{probability * 100:.1f} %")
        with col2:
            if probability > 0.5:
                st.success(ui[lang]['tier_high'])
            else:
                st.warning(ui[lang]['tier_low'])

        # --- EXECUTIVE SUMMARY (Explicabilité Bilingue) ---
        st.markdown(ui[lang]['exec_sum'])
        
        analyse = []
        
        if lang == 'FR':
            # Conclusion globale FR
            if probability > 0.8:
                analyse.append(f"**Profil d'élite.** {player_name} affiche des métriques historiques exceptionnelles pour une année rookie, le positionnant dans le percentile supérieur des futurs joueurs majeurs de la ligue.")
            elif probability > 0.5:
                analyse.append(f"**Indicateurs de développement positifs.** {player_name} démontre un potentiel solide pour atteindre le statut de All-Star, sous réserve d'optimiser certaines de ses statistiques clés.")
            else:
                analyse.append(f"**Projection conservatrice.** Les données actuelles de {player_name} le projettent vers un rôle de rotation fiable plutôt que vers un statut de franchise player.")

            # Analyse Scoring FR
            if pts >= 15.0:
                analyse.append(f"Le volume offensif est déjà un atout majeur ({pts} PTS/m), surpassant les standards de production initiaux (15 PTS) caractéristiques des stars de la ligue.")
            else:
                analyse.append(f"Le volume de scoring ({pts} PTS/m) reste un axe de progression prioritaire pour franchir le palier critique des 15 points requis pour sécuriser un statut de leader offensif.")

            # Analyse Efficacité FR
            if fg_pct >= 0.450:
                analyse.append(f"Cette production est validée par une efficacité de haut niveau ({fg_pct*100:.1f}% au tir), reflétant une sélection de tirs mature et optimisée.")
            else:
                analyse.append(f"L'efficacité au tir ({fg_pct*100:.1f}%) nécessite un ajustement, la moyenne de référence pour valider ce type de profil étant fixée à 45.0%.")

            # Analyse Volume de jeu FR
            if min_played >= 25.0:
                analyse.append(f"Son utilisation intensive ({min_played} MIN/m) indique une intégration précoce dans les schémas tactiques de l'équipe, un facteur clé de corrélation avec le développement à long terme.")
            else:
                analyse.append(f"Son plafond de développement reste conditionné par une augmentation drastique de son temps de jeu (actuellement {min_played} MIN/m) pour maximiser son impact global.")

        else:
            # Conclusion globale EN
            if probability > 0.8:
                analyse.append(f"**Elite prospect.** {player_name} displays exceptional historical metrics for a rookie year, placing them in the upper percentile of future major league players.")
            elif probability > 0.5:
                analyse.append(f"**Positive developmental indicators.** {player_name} shows solid potential to reach All-Star status, provided they optimize certain key statistics.")
            else:
                analyse.append(f"**Conservative projection.** {player_name}'s current data projects them toward a reliable rotation role rather than a franchise player status.")

            # Analyse Scoring EN
            if pts >= 15.0:
                analyse.append(f"Offensive volume is already a major asset ({pts} PPG), surpassing the initial production standards (15 PPG) characteristic of league stars.")
            else:
                analyse.append(f"Scoring volume ({pts} PPG) remains a primary area for improvement to cross the critical 15-point threshold required to secure an offensive leader status.")

            # Analyse Efficacité EN
            if fg_pct >= 0.450:
                analyse.append(f"This production is validated by high-level efficiency ({fg_pct*100:.1f}% FG), reflecting mature and optimized shot selection.")
            else:
                analyse.append(f"Shooting efficiency ({fg_pct*100:.1f}%) requires adjustment, as the benchmark average to validate this profile type is set at 45.0%.")

            # Analyse Volume de jeu EN
            if min_played >= 25.0:
                analyse.append(f"Their heavy usage ({min_played} MIN/G) indicates early integration into the team's tactical schemes, a key factor correlating with long-term development.")
            else:
                analyse.append(f"Their development ceiling remains conditional on a drastic increase in playing time (currently {min_played} MIN/G) to maximize their overall impact.")

        # Affichage du texte
        st.info(" ".join(analyse))

        # Poids des variables
        st.markdown("---")
        st.markdown(ui[lang]['feat_title'])
        st.caption(ui[lang]['feat_desc'])
        
        importances = model.feature_importances_
        features = input_data.columns
        
        feat_df = pd.DataFrame({ui[lang]['metric_col']: features, 'Importance': importances})
        feat_df = feat_df.sort_values(by='Importance', ascending=True)
        
        st.bar_chart(feat_df.set_index(ui[lang]['metric_col']))