import plotly.graph_objects as go
import streamlit as st


class PlotlyChart:
    def __init__(self, error_relativo_biseccion, error_relativo_secante, error_relativo_newton,
                 tiempo_biseccion, tiempo_secante, tiempo_newton):
        self.error_relativo_biseccion = error_relativo_biseccion
        self.error_relativo_secante = error_relativo_secante
        self.error_relativo_newton = error_relativo_newton
        self.tiempo_biseccion = tiempo_biseccion
        self.tiempo_secante = tiempo_secante
        self.tiempo_newton = tiempo_newton

    def create_figure(self):
        # Crear el gráfico
        fig = go.Figure()

        # Agregar barras para mostrar el error relativo de cada método
        fig.add_trace(go.Bar(
            x=['Bisección', 'Secante', 'Newton'],
            y=[self.error_relativo_biseccion,
                self.error_relativo_secante, self.error_relativo_newton],
            name='Error Relativo',
            marker_color='paleturquoise'
        ))

        # Agregar línea para mostrar los tiempos de ejecución de cada método
        fig.add_trace(go.Scatter(
            x=['Bisección', 'Secante', 'Newton'],
            y=[self.tiempo_biseccion, self.tiempo_secante, self.tiempo_newton],
            yaxis="y2",
            name="Tiempo de ejecución (s)",
            mode='lines+markers',
            marker=dict(color="crimson"),
        ))

        # Actualizar diseño del gráfico
        fig.update_layout(
            # Título general
            title=dict(
                text='Comparación de Métodos Numéricos',
                font=dict(color='black', size=20),
                x=0,
                y=0.9
            ),
            showlegend=True,
            legend=dict(orientation='h', font=dict(color='black')),
            yaxis=dict(
                title=dict(text="Error Relativo"),
                side="left",
            ),
            width=500,
            height=400,
            # Diseño financiero
            paper_bgcolor='rgba(0,0,0,0)',  # Fondo del papel transparente
            plot_bgcolor='rgba(0,0,0,0)',   # Fondo del gráfico transparente
            xaxis_showgrid=True,
            yaxis_showgrid=True,
            xaxis_ticks='outside',
            yaxis_ticks='outside',
            xaxis_linecolor='black',
            yaxis_linecolor='black',
            # Color de la cuadrícula del eje x con alpha
            xaxis_gridcolor='rgba(255, 255, 255, 0.1)',
            # Color de la cuadrícula del eje x con alpha
            yaxis_gridcolor='rgba(255, 255, 255, 0.1)',
            yaxis2=dict(
                title=dict(text="Tiempo de ejecución (s)"),
                side="right",
                overlaying="y",
                tickmode="auto",
                color='black'  # Color de la fuente del eje y2
            )
        )

        return fig

    def show(self):
        st.plotly_chart(self.create_figure())
