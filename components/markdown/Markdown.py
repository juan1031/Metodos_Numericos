class markdown:
    def __init__(self, texto):
        self.texto = texto

    def show(self):
        layout = f'''<div style="text-align: justify">
                        <p style="text-indent: 2em">
                            {self.texto}
                        </p>
                    </div>'''
        return layout
