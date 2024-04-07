import streamlit as st


class CenteredColumns:
    """
    Clase para crear un componente que muestra columnas centradas en Streamlit.

    Attributes:
    -----------
    num_columns : int, opcional
        El número de columnas en las que se dividirá el contenedor. Por defecto es 1.
    """

    def __init__(self, num_columns=1):
        """
        Inicializa el componente CenteredColumns.

        Parameters:
        -----------
        num_columns : int, opcional
            El número de columnas en las que se dividirá el contenedor. Por defecto es 1.
        """
        self.num_columns = num_columns

    def render(self, *args):
        num_args = len(args)

        if num_args == 0:
            st.error("Debe proporcionar al menos un objeto para centrar.")
            return

        if num_args > self.num_columns:
            st.warning(
                f"Se proporcionaron más objetos ({num_args}) que el número de columnas ({self.num_columns}). Algunos objetos pueden no mostrarse correctamente.")

        columns = st.columns(self.num_columns)

        for i, arg in enumerate(args):
            with columns[i % self.num_columns]:
                arg
