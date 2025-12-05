# src/energi_analysis/processor.py
"""Contient la logique d'extraction de données pour la visualisation GeoJSON."""

import pandas as pd
import json
import os

CSV_PATH_PROD_MENSUELLE = "data/raw/production-regionale-mensuelle-filiere-2.csv"
CSV_PATH_PROD_ANNUELLE = "data/processed/prod_annuelle_filiere_clean.csv"
GEOJSON_OUTPUT_PATH = "docs/regions.geojson"

def extract_all_regions_data():
    """
    Charge les CSV, extrait les données pour toutes les régions et tous les types d'énergie.

    :return: Un dictionnaire contenant les données pour toutes les régions.
    """
    try:
        df_prod_annuelle = pd.read_csv(CSV_PATH_PROD_ANNUELLE, sep=';')
        df_geo = pd.read_csv(CSV_PATH_PROD_MENSUELLE, sep=';').groupby('Code INSEE région').first().reset_index()

        # Pivot to get energy types as columns
        df_prod_pivot = df_prod_annuelle.pivot_table(index='code_reg', columns='filiere', values='prod_mwh', aggfunc='sum').reset_index()
        df_prod_pivot.fillna(0, inplace=True);

        # Merge with geo data
        df_merged = pd.merge(df_geo, df_prod_pivot, left_on='Code INSEE région', right_on='code_reg', how='left')

        all_regions_data = []
        for index, row in df_merged.iterrows():
            if pd.notna(row['Géo-point région']):
                geo_point_str = row['Géo-point région']
                lat, lon = map(float, geo_point_str.split(','))

                data = {
                    "regionCode": int(row['Code INSEE région']),
                    "regionName": row['Région'],
                    "regionCenter": [lat, lon],
                    "productions": {
                        "Nucléaire": row.get('Nucléaire', 0),
                        "Thermique": row.get('Thermique', 0),
                        "Hydraulique": row.get('Hydraulique', 0),
                        "Eolien": row.get('Eolien', 0),
                        "Solaire": row.get('Solaire', 0),
                        "Bioénergies": row.get('Bio-énergies', 0), # Note the key name
                        "Total": row.get('Total', 0)
                    }
                }
                all_regions_data.append(data)
        
        return {"data": all_regions_data}

    except FileNotFoundError as e:
        return {"error": f"Fichier non trouvé: {e}. Vérifiez l'emplacement des CSV."}
    except Exception as e:
        return {"error": f"Erreur de traitement des données: {e}"}

def save_all_regions_geojson():
    """
    Extrait les données GeoJSON pour toutes les régions et les sauvegarde dans un fichier
    sous forme de FeatureCollection, avec les données de production.
    """
    try:
        df_prod_annuelle = pd.read_csv(CSV_PATH_PROD_ANNUELLE, sep=';')
        df_geo = pd.read_csv(CSV_PATH_PROD_MENSUELLE, sep=';').groupby('Code INSEE région').first().reset_index()
        
        df_prod_pivot = df_prod_annuelle.pivot_table(index='code_reg', columns='filiere', values='prod_mwh', aggfunc='sum').reset_index()
        df_prod_pivot.fillna(0, inplace=True);
        df_prod_pivot['Total'] = df_prod_pivot.drop(columns='code_reg').sum(axis=1)


        df_merged = pd.merge(df_geo, df_prod_pivot, left_on='Code INSEE région', right_on='code_reg', how='left')

        features = []
        for index, row in df_merged.iterrows():
            if pd.notna(row['Géo-shape région']):
                geojson_str = row['Géo-shape région']
                try:
                    geometry = json.loads(geojson_str)
                except json.JSONDecodeError:
                    continue
                
                properties = {
                    "regionCode": int(row['Code INSEE région']),
                    "regionName": row['Région']
                }
                
                # Add productions to properties
                for col in df_prod_pivot.columns:
                    if col != 'code_reg':
                        value = row.get(col, 0)
                        properties[col] = value if pd.notna(value) else None

                feature = {
                    "type": "Feature",
                    "properties": properties,
                    "geometry": geometry
                }
                features.append(feature)

        feature_collection = {
            "type": "FeatureCollection",
            "features": features
        }

        os.makedirs(os.path.dirname(GEOJSON_OUTPUT_PATH), exist_ok=True)
        with open(GEOJSON_OUTPUT_PATH, 'w') as f:
            json.dump(feature_collection, f)
        
        if not os.path.exists(GEOJSON_OUTPUT_PATH):
            return {"error": f"Le fichier {GEOJSON_OUTPUT_PATH} n'a pas été créé."}
            
        return {"success": True, "path": os.path.abspath(GEOJSON_OUTPUT_PATH)}
    except Exception as e:
        return {"error": f"Erreur lors de la sauvegarde du GeoJSON de toutes les régions: {e}"}

# Ajoutez ici d'autres classes ou fonctions de nettoyage/traitement
# class EnergyDataset: ...