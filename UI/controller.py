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

        minimo_importo = self._view.importo_medio_minimo.value
        if isinstance(minimo_importo, str) or minimo_importo < 0:
            self._view.show_alert("L'importo medio minimo deve essere un numero maggiore o uguale a zero!")
        else:

            self._view.lista_visualizzazione.controls.clear()


        # TODO modificare qui per prendere le cose dal model e stamparle nella ListView nella view
