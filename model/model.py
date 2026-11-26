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
        if self._nodes is None:
            self._nodes = DAO.get_filiali()

        for filiale in self._nodes:
            self._dizionario_nodi[filiale.id] = filiale


    def costruisci_grafo(self, threshold):
        """
        Costruisce il grafo (self.G) inserendo tutte le Filiali (i nodi) presenti e filtrando i Collegamenti con
        importo medio per bonifico >= threshold (euro)
        """

        self.G.add_nodes_from(self._nodes)  # Aggiungo i nodi

        # Mi restituisce una lista di dizionari (dictionary = True):
        # [{"id_filiale_origine":1, "id_filiale_destinazione": 2, "importo_tot": 300, "num_bonifici": 3}, {...}]
        bonifici = DAO.get_bonifici()

        # Il risultato della query tiene conto dell'ordine (A->B != B->A)
        # quindi devo gestirlo qui

        dict_bonifici = {} # Dizionario che ha come chiavi le tuple di coppie di id orgine e destinazione, come valori un lista con 2 elementi: somma degli importi e numero di importi

        for bonifico in bonifici:
            id_origine = bonifico["id_filiale_origine"]
            id_destinazione = bonifico["id_filiale_destinazione"]
            if (id_origine, id_destinazione) in dict_bonifici.keys():
                dict_bonifici[(id_origine, id_destinazione)][0] += bonifico["importo_tot"]
                dict_bonifici[(id_origine, id_destinazione)][1] += bonifico["num_bonifici"]
            elif (id_destinazione, id_origine) in dict_bonifici.keys():
                dict_bonifici[(id_destinazione, id_origine)][0] += bonifico["importo_tot"]
                dict_bonifici[(id_destinazione, id_origine)][1] += bonifico["num_bonifici"]
            else:
                dict_bonifici[(id_origine, id_destinazione)] = [bonifico["importo_tot"], bonifico["num_bonifici"]]

        for tupla_id, lista_valori in dict_bonifici.items():
            u = self._dizionario_nodi[tupla_id[0]]
            v = self._dizionario_nodi[tupla_id[1]]
            importo_medio = lista_valori[0] / lista_valori[1]
            if importo_medio >= threshold:
                self.G.add_edge(u, v, peso = importo_medio)




    def get_num_edges(self):
        """
        Restituisce il numero di Collegamenti (edges) del grafo
        :return: numero di edges del grafo
        """
        num_edges = 0
        for _ in self.G.edges():
            num_edges += 1
        return num_edges

    def get_num_nodes(self):
        """
        Restituisce il numero di Filiali (nodi) del grafo
        :return: numero di nodi del grafo
        """
        num_nodi = 0
        for _ in self.G.nodes():
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
            edges.append((u, v, attrs.get('peso')))
        return edges



# TODO quando creo una volta il grafo poi si ricrea o no ? controllare
