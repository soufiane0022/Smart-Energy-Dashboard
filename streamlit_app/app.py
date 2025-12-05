import streamlit as st
import pandas as pd
from src.data_loader import load_data, get_region_coordinates
import plotly.express as px
import folium
from streamlit_folium import st_folium

# Use the wide layout and a more modern theme
st.set_page_config(layout="wide", page_title="EnergiFrance Dashboard")

@st.cache_data
def get_all_data():
    dataframes = load_data()
    region_coords_df = get_region_coordinates()
    
    # Merge bilan_energetique with region_coords_df to add latitude and longitude
    dataframes['bilan_energetique'] = pd.merge(
        dataframes['bilan_energetique'], 
        region_coords_df, 
        left_on='code_reg', 
        right_on='code_région', 
        how='left'
    )
    dataframes['bilan_energetique'].drop(columns=['code_région'], inplace=True)

    return dataframes

def main():
    st.sidebar.title("EnergiFrance")
    st.sidebar.info(
        """
        Ce tableau de bord interactif visualise la production et la consommation 
        d'énergie en France, ainsi que la part des énergies renouvelables.
        """
    )
    page = st.sidebar.radio("Navigation", ["Consommation", "Mix énergétique", "Carte interactive"])

    dataframes = get_all_data()

    if page == "Consommation":
        st.title("⚡ Consommation d'électricité en France")
        
        conso_df = dataframes['conso_clean_dept']
        
        col1, col2 = st.columns([2, 1])

        with col1:
            st.subheader("Évolution de la consommation totale")
            # Aggregate consumption by year
            conso_annuelle = conso_df.groupby('annee')['conso_totale'].sum().reset_index()
            
            fig = px.line(
                conso_annuelle, 
                x='annee', 
                y='conso_totale', 
                title="Consommation totale d'électricité en France (en MWh)",
                labels={'annee': 'Année', 'conso_totale': 'Consommation (MWh)'}
            )
            fig.update_layout(
                plot_bgcolor='rgba(0,0,0,0)', 
                paper_bgcolor='rgba(0,0,0,0)',
                font_color="white"
            )
            st.plotly_chart(fig, use_container_width=True)

        with col2:
            st.subheader("Top 5 des départements consommateurs")
            top_5_dept = conso_df.groupby('nom_dept')['conso_totale'].sum().nlargest(5).reset_index()
            st.dataframe(top_5_dept, hide_index=True)


    elif page == "Mix énergétique":
        st.title("Mix énergétique en France")
        
        prod_annuelle_df = dataframes['prod_annuelle_filiere_clean']

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Répartition de la production par filière")
            # Aggregate production by energy source
            prod_by_filiere = prod_annuelle_df.groupby('filiere')['prod_gwh'].sum().reset_index()
            
            fig = px.pie(
                prod_by_filiere, 
                values='prod_gwh', 
                names='filiere', 
                title="Production d'énergie par filière (en GWh)",
                hole=.3
            )
            fig.update_layout(
                plot_bgcolor='rgba(0,0,0,0)', 
                paper_bgcolor='rgba(0,0,0,0)',
                font_color="white"
            )
            st.plotly_chart(fig, use_container_width=True)
            
        with col2:
            st.subheader("Production annuelle par filière")
            st.dataframe(prod_annuelle_df, hide_index=True)


    elif page == "Carte interactive":
        st.title("🗺️ Carte interactive de la production et consommation d'énergie")

        bilan_df = dataframes['bilan_energetique']
        bilan_df.dropna(subset=['latitude', 'longitude'], inplace=True)

        st.info("Zoomez et cliquez sur les cercles pour plus de détails.")

        m = folium.Map(location=[46.603354, 1.888334], zoom_start=6, tiles="CartoDB dark_matter")

        for _, row in bilan_df.iterrows():
            color = row.get('couleur_carte', 'gray').lower() 
            if color not in ['red', 'orange', 'green']:
                color = 'gray'

            popup_html = f"""
            <b>Région:</b> {row['nom_region']}<br>
            <b>Production (MWh):</b> {row['prod_mwh']:.2f}<br>
            <b>Consommation (MWh):</b> {row['conso_totale']:.2f}<br>
            <b>Taux de couverture:</b> {row['taux_couverture']:.2f}%
            """
            
            folium.CircleMarker(
                location=[row['latitude'], row['longitude']],
                radius=row['taux_couverture']/10,  # Scale radius by coverage rate
                popup=folium.Popup(popup_html, max_width=300),
                color=color,
                fill=True,
                fill_color=color,
                fill_opacity=0.7
            ).add_to(m)

        st_folium(m, use_container_width=True)

if __name__ == "__main__":
    main()