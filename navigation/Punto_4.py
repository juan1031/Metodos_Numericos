import streamlit as st
import pandas as pd
from src.OLSRegression import RegressionMetrics
import statsmodels.formula.api as sm
import hydralit_components as hc


def punto_cuatro():

    file1 = open('./data/punto_4/contexto_mco.md').read()
    data = pd.read_csv('./data/punto_4/base_p4.csv', index_col=0)
    data = data.drop('fatheduc', axis=1)
    data = data.dropna(subset=['motheduc'])
    data = data[['faminc', 'cigprice', 'bwght', 'motheduc', 'male', 'cigs']]
    data1 = data.copy()
    # -------------------------------------------------------------
    # NavBar

    a = 'Introducción'
    b = 'EDA'
    c = 'Modelos'

    tabs = [
        a,
        b,
        c
    ]

    option_data = [
        {'icon': "", 'label': a},
        {'icon': "", 'label': b},
        {'icon': "", 'label': c}
    ]

    # Define el tema para el NavBar
    theme = {
        'menu_background': '#1a1a1a',  # Color de fondo del menú
        'txc_inactive': '#999999',  # Color del texto de las pestañas inactivas
        'txc_active': 'white',  # Color del texto de la pestaña activa
        'option_active': '#007bff'  # Color de la pestaña activa
    }

    # Crea el NavBar con los datos y el tema especificados
    chosen_tab = hc.option_bar(
        option_definition=option_data,
        title='',
        key='PrimaryOptionx2',
        override_theme=theme,
        horizontal_orientation=True)

    if chosen_tab == a:

        st.markdown(file1)

        st.divider()

    if chosen_tab == b:

        st.image('./data/punto_4/EDA_metodos.png',
                 caption='EDA de la base de datos')

        st.divider()

    if chosen_tab == c:

        col1, col2 = st.columns([3, 2])

        with col1:

            regression = RegressionMetrics(data, 'bwght')
            regression.fit()
            regression.display_metrics()
            

        with col2:

            formula = 'bwght ~ faminc + cigprice + motheduc + male + cigs'
            model = sm.ols(formula=formula, data=data1)
            fitted = model.fit()

            coefs = fitted.params
            std_errors = fitted.bse
            variable_names = coefs.index.tolist()
            R_squared = fitted.rsquared

            st.text("=" * 54)
            st.text("{:<12} {:>20} {:>20}".format(
                "Variable", "Coef", "Standard Error"))
            st.text("-" * 54)

            for nombre, coeficiente, error in zip(variable_names, coefs, std_errors):
                st.text("{:<12} {:>20.15f} {:>20.15f}".format(
                    nombre, coeficiente, error))

            st.text("=" * 54)
            st.text("R-squared: {}".format(R_squared))

        st.divider()
    # -------------------------------------------------------------
