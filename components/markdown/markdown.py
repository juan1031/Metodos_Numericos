class Markdown:
    def __init__(self, texto):
        self.texto = texto

    def show(self, tab=True):
        '''
        Si tab=True va tener identación a la izquierda el texto.
        Si tab=False no va tener identación.
        '''
        if tab:
            layout = f'<div style="text-align: justify; max-width: 100%; display: block;">' \
                     f'<p style="text-indent: 2em">{self.texto}</p></div>'
        else:
            layout = f"""<div style="text-align: justify; max-width: 100%; display: block;">{self.texto}</div>"""

        return layout
