import pandas as pd
import plotly.express as px
import os
from pathlib import Path

def annual_production_by_filiere_chart(project_root: Path):
    """Generates the annual production by filiere chart and saves it as an HTML file."""
    data_path = project_root / 'data' / 'processed' / 'prod_annuelle_filiere_clean.csv'
    df = pd.read_csv(data_path, sep=';')
    df_filtered = df[(df['nom_reg'] == 'Bretagne') & (df['annee'] == 2021)]
    fig = px.pie(df_filtered,
                 values='prod_mwh',
                 names='filiere',
                 title='Production par Filière en Bretagne (2021)',
                 labels={'prod_mwh': 'Production (MWh)', 'filiere': 'Filière'})
    
    charts_dir = project_root / 'docs' / 'charts'
    os.makedirs(charts_dir, exist_ok=True)
    fig.write_html(charts_dir / "annual_production_by_filiere.html")

def filiere_production_evolution_chart(project_root: Path):
    """Generates the filiere production evolution chart and saves it as an HTML file."""
    data_path = project_root / 'data' / 'processed' / 'prod_annuelle_filiere_clean.csv'
    df = pd.read_csv(data_path, sep=';')
    df_filtered = df[(df['filiere'] == 'Eolien') & (df['nom_reg'] == 'Bretagne')]
    fig = px.line(df_filtered,
                  x='annee',
                  y='prod_mwh',
                  title='Évolution de la Production Éolienne en Bretagne',
                  labels={'prod_mwh': 'Production (MWh)', 'annee': 'Année'})
    
    charts_dir = project_root / 'docs' / 'charts'
    os.makedirs(charts_dir, exist_ok=True)
    fig.write_html(charts_dir / "filiere_production_evolution.html")

def monthly_production_chart(project_root: Path):
    """Generates the monthly production chart and saves it as an HTML file."""
    data_path = project_root / 'data' / 'processed' / 'prod_mensuelle_clean.csv'
    df = pd.read_csv(data_path, sep=';')
    df_filtered = df[(df['nom_reg'] == 'Bretagne') & (df['annee'] == 2021) & (df['filiere'] == 'Eolien')]
    fig = px.line(df_filtered,
                  x='mois_num',
                  y='prod_mwh',
                  title='Production Mensuelle Éolienne en Bretagne (2021)',
                  labels={'prod_mwh': 'Production (MWh)', 'mois_num': 'Mois'})
    
    charts_dir = project_root / 'docs' / 'charts'
    os.makedirs(charts_dir, exist_ok=True)
    fig.write_html(charts_dir / "monthly_production.html")
