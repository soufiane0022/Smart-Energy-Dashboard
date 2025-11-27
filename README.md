#  EnergiFrance

---
title: "EnergiFrance"
format: html
---

#  EnergiFrance

##  Site Web

 [**Accéder au site du projet EnergiFrance**](https://soufiane0022.github.io/EnergiFrance/)

---

## Description du projet / Objectif

Le projet **EnergiFrance** a pour objectif de visualiser la production et la consommation d’énergie en France, ainsi que la part des énergies renouvelables (solaire, éolien, hydraulique, etc.), à partir de données publiques fournies par **RTE** et **ENEDIS**.

Notre but est d'élaborer un **site web interactif** permettant :

- de suivre l’évolution de la consommation et de la production d’électricité sur plusieurs périodes (jour, semaine, mois) ;
- de visualiser la répartition par type d’énergie à travers des graphiques clairs et dynamiques ;
- d’afficher une carte de la France interactive, montrant la production ou la consommation région par région ;
- et, à terme, d’intégrer un modèle de prévision de la consommation future à court terme.

Pour rendre l’expérience intuitive, nous mettrons en place :

- un **code couleur** indiquant la part d’énergie renouvelable :  
  🟩 vert : forte part d’énergie renouvelable  
  🟧 orange : part moyenne  
  🟥 rouge : faible part renouvelable  
- plusieurs **onglets dans le tableau de bord** :  
  - **Consommation** : évolution de la consommation d’électricité dans le temps.  
  - **Mix énergétique** : répartition des différentes sources d’énergie (nucléaire, solaire, éolien, hydraulique, etc.).  
  - **Carte interactive** : vision régionale de la production et de la consommation sur la carte de France.

---

##  Membres de l'équipe et rôles

| Nom | Rôle |
|------|------|
| Yonkeu-Waya Kevin-Roseverlt | Extraction, nettoyage et intégration des données |
| Soumah Ousmane | Visualisation et analyse |
| Enniya Soufiane | Développement du tableau de bord et interface web |
| Assoumani Ben-enfane | Documentation et coordination |

---
##  Jeux de données utilisés

- **RTE Open Data** – Production et consommation d’électricité par type d’énergie.  
- **ENEDIS Open Data** – Données locales et régionales de consommation.  
- **INSEE** – Données démographiques et structurelles par région.

---


##  Choix des packages

- **Pandas** : lire et manipuler les données CSV (RTE, ENEDIS, INSEE).  
- **NumPy** : effectuer des calculs statistiques et des agrégations.  
- **Plotly** : créer des graphiques interactifs.  
- **Streamlit** : concevoir une interface interactive.  
- **GeoPandas** : manipuler les données géographiques (régions de France).  
- **Folium** : afficher la carte de France avec les régions colorées selon la production.  
- **Matplotlib** : produire des graphiques statiques.  
- **Requests** : télécharger les données publiques depuis les API.  
- **OpenPyXL** : lire/exporter les fichiers Excel.  
- **Jupyter / Quarto** : générer la documentation et tester les fonctions.

---

##  Choix des langages

- **Python**  
- **HTML**

---

## Pipeline de développement

1. **Acquisition des données** : récupération des jeux RTE, ENEDIS, INSEE.  
2. **Nettoyage et prétraitement** : suppression des doublons, valeurs manquantes.  
3. **Analyse exploratoire** : étude des tendances et corrélations.  
4. **Visualisations** : création des graphiques, cartes et indicateurs.  
5. **Tableau de bord** : intégration dans une interface Streamlit.  
6. **Documentation** : rédaction et hébergement sur GitHub Pages.  
7. **Collaboration Git** :  le développement est organisé en plusieurs branches, chacune dédiée à une tâche spécifique (traitement des données, visualisation, interface web, documentation), ce qui permet un travail parallèle et une intégration progressive dans la branche principale
    

##  Diagramme de Gantt

```{mermaid}
gantt
    dateFormat  YYYY-MM-DD
    title Smart Energy Dashboard – Planification du projet
    todayMarker off

    %% PHASE 1 – Lancement du projet
    section Démarrage
     choix du projet                  :done, a1, 2025-10-17, 3d
    Création du dépôt GitHub,des branches et Répartition des tâches et planification
         :done, a2, 2025-10-22, 2d
    Rédaction de la roadmap initiale                 :a4, 2025-10-24, 5d

    %% PHASE 2 – Données et préparation
    section Données
    Recherche et sélection des jeux de données       :a5, 2025-10-28, 5d
    Extraction et nettoyage des données              :a6, 2025-11-02, 7d
    Vérification et intégration dans le dépôt        :a7, 2025-11-09, 4d

    %% PHASE 3 – Développement et visualisation
    section Développement
    Analyse exploratoire des données                 :a8, 2025-11-13, 5d
    Création des premiers graphiques                 :a9, 2025-11-18, 5d
    Carte interactive de la France                   :a10, 2025-11-23, 6d
    Développement du tableau de bord Streamlit       :a11, 2025-11-29, 6d
    Intégration des visualisations dans le site      :a12, 2025-12-04, 4d

    %% PHASE 4 – Documentation et tests
    section Documentation
    Rédaction des docstrings et commentaires         :a13, 2025-12-08, 3d
    Préparation du README final et Gantt             :a14, 2025-12-11, 3d
    Mise en ligne sur GitHub Pages                   :a15, 2025-12-14, 2d

    %% PHASE 5 – Validation et soutenance
    section Finalisation
    Tests finaux et corrections                      :a16, 2025-12-16, 3d
    Répétition de la présentation                    :a17, 2025-12-19, 2d
    Soutenance finale et dépôt du projet             :a18, 2025-12-22, 1d
---


    


