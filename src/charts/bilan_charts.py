import pandas as pd
import plotly.express as px
import os
from pathlib import Path

def consumption_vs_production_chart(project_root: Path):
    """Generates the consumption vs production chart and saves it as an HTML file."""
    data_path = project_root / 'data' / 'processed' / 'bilan_energetique.csv'
    df = pd.read_csv(data_path, sep=';')
    fig = px.bar(df,
                 x='nom_region',
                 y=['conso_totale', 'prod_mwh'],
                 title='Consommation vs. Production par Région (2014-2022)',
                 labels={'value': 'Énergie (MWh)', 'variable': 'Type'},
                 barmode='group')
    
    # Create the directory if it doesn't exist
    charts_dir = project_root / 'docs' / 'charts'
    os.makedirs(charts_dir, exist_ok=True)
    fig.write_html(charts_dir / "consumption_vs_production.html")

def coverage_rate_chart(project_root: Path):
    """Generates the coverage rate chart and saves it as an HTML file."""
    data_path = project_root / 'data' / 'processed' / 'bilan_energetique.csv'
    df = pd.read_csv(data_path, sep=';')
    fig = px.bar(df,
                 x='nom_region',
                 y='taux_couverture',
                 color='couleur_carte',
                 title='Taux de Couverture Énergétique par Région (2014-2022)',
                 labels={'taux_couverture': 'Taux de Couverture (%)', 'nom_region': 'Région'},
                 color_discrete_map={'Vert': 'green', 'Rouge': 'red', 'Orange': 'orange'})
    
    # Create the directory if it doesn't exist
    charts_dir = project_root / 'docs' / 'charts'
    os.makedirs(charts_dir, exist_ok=True)
    fig.write_html(charts_dir / "coverage_rate.html")
