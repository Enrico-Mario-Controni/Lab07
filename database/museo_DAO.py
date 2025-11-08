from database.DB_connect import ConnessioneDB
from model.museoDTO import Museo

"""
    Museo DAO
    Gestisce le operazioni di accesso al database relative ai musei (Effettua le Query).
"""

class MuseoDAO:
    def __init__(self):
        pass

    # TODO
    @staticmethod
    def musei():
        musei=[]
        cnx= ConnessioneDB.get_connection()
        cursor = cnx.cursor()
        query= """SELECT * FROM museo"""
        cursor.execute(query)
        righe = cursor.fetchall()
        for museo in righe:
            musei.append( Museo(museo[0],museo[1],museo[2]) )

        cnx.close()
        cursor.close()
        return musei
