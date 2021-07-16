from model.dao.dao import DAO
from model.dbconnector import DBConnector
from shared.iPetri import IPetri


class DAOPetri(DAO):
    def __init__(self, dbConnector: DBConnector):
        DAO.__init__(self, dbConnector, "Petris")

    def save(self, petri: IPetri):

        self.getCollection().insert({"test": "Test réussi"})
