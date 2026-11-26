import flet as ft
from UI.view import View
from model.model import Model


class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model

    def mostra_collegamenti(self, e):
        """
        Funzione che controlla prima se il valore dell'importo inserito sia valido (es. non deve essere una stringa) e
        poi popola "self._view.lista_visualizzazione" con le seguenti info
        * Numero di Filiali presenti
        * Numero di Collegamenti
        * Lista di Collegamenti che superano l'importo indicato come soglia
        """

        try:
            minimo_importo = float(self._view.importo_medio_minimo.value)
            if minimo_importo < 0:
                self._view.show_alert("L'importo medio minimo deve essere un numero maggiore o uguale a zero!")
            else:
                self._model.costruisci_grafo(minimo_importo)

                self._view.lista_visualizzazione.controls.clear()
                self._view.lista_visualizzazione.controls.append(ft.Text(f"Numero di Filiali: {self._model.get_num_nodes()}"))
                self._view.lista_visualizzazione.controls.append(ft.Text(f"Numero di Collegamenti: {self._model.get_num_edges()}"))
                self._view.update()

                for i, arco in enumerate(self._model.get_all_edges()):
                    self._view.lista_visualizzazione.controls.append(ft.Text(f"{i+1}) [{arco[0]} -> {arco[1]}] -- Importo medio per bonifico: €{arco[2]:.2f}"))

                self._view.update()
        except ValueError:
            self._view.show_alert("Inserisci un numero")


