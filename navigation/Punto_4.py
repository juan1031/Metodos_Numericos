import streamlit as st
import pandas as pd
from src.OLSRegression import RegressionMetrics
import statsmodels.formula.api as sm
import hydralit_components as hc


def punto_cuatro():

    file1 = open('./data/punto_4/contexto_mco.md').read()
    file2 = open('./data/punto_4/problema.md').read()
    file3 = open('./data/punto_4/modelos.md').read()

    st.markdown(file1)

    data = pd.read_csv('./data/punto_4/base_p4.csv', index_col=0)
    data = data.drop('fatheduc', axis=1)
    data = data.dropna(subset=['motheduc'])

    # -------------------------------------------------------------
    # NavBar

    a = 'Introducción & EDA'
    c = 'Modelos'

    tabs = [
        a,
        c
    ]

    option_data = [
        {'icon': "", 'label': a},
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

        st.markdown(file2)

        st.divider()

        _, col, _ = st.columns([.5, 3, .5])
        with col:
            st.image('./data/punto_4/EDA_metodos.png',
                     caption='EDA de la base de datos')

        st.divider()

    if chosen_tab == c:

        st.markdown(file3)
        _, col, _ = st.columns([.5, 3, .5])
        with col:
            st.dataframe(data=data, width=1000, height=300)

        # Menú desplegable para seleccionar las empresas
        selected_vars = st.multiselect(
            "Selecciona las variables que quieres usar para el modelo: ", data.drop(
                'bwght', axis=1).columns.to_list(),
            default=['faminc', 'cigprice',
                     'motheduc', 'male', 'cigs'],
        )

        if not selected_vars:
            st.warning("Por favor, selecciona al menos una variable.")
            st.stop()

        todas = selected_vars.copy()
        todas.append('bwght')

        data1 = data[todas]

        col1, _, col2 = st.columns([3, .5, 3])

        with col1:

            st.subheader('Metodos Numéricos')
            regression = RegressionMetrics(data1, 'bwght')
            regression.fit()
            regression.display_metrics()

            with st.expander("Ver script MCO con metodos numericos"):

                with open("./src/OLSRegression.py", "r") as file:
                    script_content = file.read()

                st.code(script_content, language="python")

        with col2:

            st.subheader('Modulo Statsmodels')
            formula = 'bwght ~ ' + ' + '.join(selected_vars)
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

            code = '''
                    # selected_vars es la lista de variables del menú

                    formula = 'bwght ~ ' + ' + '.join(selected_vars)
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

                    '''
            with st.expander("Ver script MCO Stats Model"):

                st.code(code, language="python")

        st.divider()
    # -------------------------------------------------------------
