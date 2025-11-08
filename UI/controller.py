import flet as ft
from UI.view import View
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.museo_selezionato = None
        self.epoca_selezionata = None

    # POPOLA DROPDOWN
    # TODO
    def dd_popola_museo(self):
        lista_musei=Model.get_musei()
        opzioni_musei=[]
        for n, museo in enumerate(lista_musei, start=1):
            opzioni_musei.append(ft.dropdown.Option(key=str(n), text=museo))

        opzioni_musei.append(ft.dropdown.Option(key="0", text="Null"))


        return opzioni_musei

    def dd_epoca_museo(self):
        lista_epoche=Model.get_epoche()
        opzioni_epoche=[]
        for epoca in lista_epoche:
            opzioni_epoche.append(ft.dropdown.Option(epoca))

        opzioni_epoche.append(ft.dropdown.Option("Null"))
        return opzioni_epoche

    # CALLBACKS DROPDOWN
    # TODO
    def callbacks_museo(self,e):
        self.museo_selezionato = e.control.value
        print(self.museo_selezionato)
        return self.museo_selezionato


    def callbacks_epoca(self,e):
        self.epoca_selezionata = e.control.value
        print(self.epoca_selezionata)
        return self.epoca_selezionata


    # AZIONE: MOSTRA ARTEFATTI
    # TODO
    def callbacks_view(self,e):
        lista_filtrata=self._model.get_artefatti_filtrati(
            self.museo_selezionato,
            self.epoca_selezionata)

        self._view.lista.controls.clear()
        for el in lista_filtrata:
            testo= ft.Text(f"{el}")
            self._view.lista.controls.append(testo)

        if not lista_filtrata:
            self._view.show_alert("Nessun artefatto trovato con questi filtri!")

        self._view.page.update()

