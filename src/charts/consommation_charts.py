import pandas as pd
import plotly.express as px
import os
from pathlib import Path

def consumption_by_sector_chart(project_root: Path):
    """Generates the consumption by sector chart and saves it as an HTML file."""
    data_path = project_root / 'data' / 'processed' / 'conso_clean_dept.csv'
    df = pd.read_csv(data_path, sep=';')
    df_filtered = df[(df['nom_dept'] == 'Aude') & (df['annee'] == 2014)]
    df_melted = df_filtered.melt(id_vars=['nom_dept', 'annee'],
                                 value_vars=['Consommation agriculture (MWh)',
                                             'Consommation industrie (MWh)',
                                             'Consommation résidentiel (MWh)',
                                             'Consommation tertiaire (MWh)',
                                             'Consommation autre (MWh)'],
                                 var_name='secteur',
                                 value_name='consommation')
    fig = px.bar(df_melted,
                 x='secteur',
                 y='consommation',
                 title='Consommation par Secteur dans l\'Aude (2014)',
                 labels={'consommation': 'Consommation (MWh)', 'secteur': 'Secteur'})
    
    charts_dir = project_root / 'docs' / 'charts'
    os.makedirs(charts_dir, exist_ok=True)
    fig.write_html(charts_dir / "consumption_by_sector.html")

def total_consumption_breakdown_chart(project_root: Path):
    """Generates the total consumption breakdown chart and saves it as an HTML file."""
    data_path = project_root / 'data' / 'processed' / 'conso_clean_dept.csv'
    df = pd.read_csv(data_path, sep=';')
    df_agg = df.groupby('nom_dept')[['Consommation agriculture (MWh)',
                                       'Consommation industrie (MWh)',
                                       'Consommation résidentiel (MWh)',
                                       'Consommation tertiaire (MWh)',
                                       'Consommation autre (MWh)']].sum().reset_index()
    df_melted = df_agg.melt(id_vars='nom_dept',
                            value_vars=['Consommation agriculture (MWh)',
                                        'Consommation industrie (MWh)',
                                        'Consommation résidentiel (MWh)',
                                        'Consommation tertiaire (MWh)',
                                        'Consommation autre (MWh)'],
                            var_name='secteur',
                            value_name='consommation')
    fig = px.bar(df_melted,
                 x='nom_dept',
                 y='consommation',
                 color='secteur',
                 title='Répartition de la Consommation par Secteur et Département',
                 labels={'consommation': 'Consommation (MWh)', 'nom_dept': 'Département'},
                 barmode='stack')
    
    charts_dir = project_root / 'docs' / 'charts'
    os.makedirs(charts_dir, exist_ok=True)
    fig.write_html(charts_dir / "total_consumption_breakdown.html")

