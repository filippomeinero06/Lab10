from database.DB_connect import DBConnect
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
