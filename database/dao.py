from database.DB_connect import DBConnect
from model.bonifico import Bonifico
from model.filiale import Filiale


class DAO:
    """
        Implementare tutte le funzioni necessarie a interrogare il database.
    """

    @staticmethod
    def get_filiali():
        conn = DBConnect.get_connection()
        try:
            cursor = conn.cursor(dictionary=True)
            try:
                query = "SELECT id, codice, nome, citta, provincia, latitudine, longitudine FROM filiale"
                cursor.execute(query)
                result = []
                for row in cursor:
                    filiale = Filiale(row["id"], row["codice"], row["nome"], row["citta"], row["provincia"], row["latitudine"], row["longitudine"])
                    result.append(filiale)
                return result
            finally:
                cursor.close()
        finally:
            conn.close()

    @staticmethod
    def get_bonifici():
        conn = DBConnect.get_connection()
        try:
            cursor = conn.cursor(dictionary=True)
            try:
                query = """SELECT id_filiale_origine, id_filiale_destinazione, SUM(importo) AS importo_tot, COUNT(*) AS num_bonifici
                            FROM bonifico 
                            GROUP BY id_filiale_origine, id_filiale_destinazione 
                            """
                cursor.execute(query)
                result = []
                for row in cursor:
                    result.append(row)
                return result
            finally:
                cursor.close()
        finally:
            conn.close()
