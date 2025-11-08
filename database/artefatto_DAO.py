from database.DB_connect import ConnessioneDB
from model.artefattoDTO import Artefatto

"""
    ARTEFATTO DAO
    Gestisce le operazioni di accesso al database relative agli artefatti (Effettua le Query).
"""

class ArtefattoDAO:
    def __init__(self):
        pass

    # TODO
    @staticmethod
    def artefatto( museo:str, epoca:str):
        artefatto=[]
        cnx= ConnessioneDB.get_connection()
        cursor = cnx.cursor()
        query = """SELECT * FROM artefatto 
                 WHERE epoca = COALESCE(%s, epoca) and id_museo IN(SELECT id_museo FROM museo 
                                                                    WHERE id_museo =  COALESCE(%s, id_museo))
                 """
        cursor.execute(query,(epoca,museo,))
        righe = cursor.fetchall()
        for artefatti in righe:
            artefatto.append(Artefatto(artefatti[0], artefatti[1], artefatti[2], artefatti[3], artefatti[4]))

        cnx.close()
        cursor.close()
        return artefatto



    @staticmethod
    def epoche():
        epoche=[]
        cnx= ConnessioneDB.get_connection()
        cursor = cnx.cursor()
        query = "SELECT DISTINCT epoca FROM artefatto"
        cursor.execute(query)
        righe = cursor.fetchall()
        for el in righe:
            epoche.append(el[0])

        cnx.close()
        cursor.close()
        return epoche