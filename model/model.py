from database.dao import DAO
import networkx as nx

class Model:
    def __init__(self):
        self._nodes = None
        self._edges = None

        self._dizionario_nodi = {}
        self.popola_nodes() # Popolo la lista e il dizionario di nodi (filiali)

        self.G = nx.Graph()



    def popola_nodes(self):
        self._nodes = DAO.get_filiali()

        for filiale in self._nodes:
            self._dizionario_nodi[filiale.id] = filiale


    def costruisci_grafo(self, threshold):
        """
        Costruisce il grafo (self.G) inserendo tutte le Filiali (i nodi) presenti e filtrando i Collegamenti con
        importo medio per bonifico >= threshold (euro)
        """

        self.G.add_nodes_from(self._nodes)  # Aggiungo i nodi

        # TODO capire come aggiungere gli edges



    def get_num_edges(self):
        """
        Restituisce il numero di Collegamenti (edges) del grafo
        :return: numero di edges del grafo
        """
        num_edges = 0
        for edge in self.G.edges():
            num_edges += 1
        return num_edges

    def get_num_nodes(self):
        """
        Restituisce il numero di Filiali (nodi) del grafo
        :return: numero di nodi del grafo
        """
        num_nodi = 0
        for filiale in self.G.nodes():
            num_nodi += 1
        return num_nodi

    def get_all_edges(self):
        """
        Restituisce tutti i Collegamenti (gli edges) con i corrispondenti pesi
        :return: gli edges del grafo con gli attributi (il weight)
        """
        edges = []
        # Cicla solo sugli archi che esistono davvero nel grafo
        for u, v, attrs in self.G.edges(data=True):
            edges.append((u, v, attrs.get('weight')))



