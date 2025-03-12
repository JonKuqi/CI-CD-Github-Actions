import json
from paths import ROOT_DIR, root_join


class DataFetcher:

    @staticmethod
    def getBooks():
        dataFileBooks = root_join("Data", "Books.json")
        with open(dataFileBooks, 'r') as file:
            return json.load(file)

    @staticmethod
    def getUsers():
        dataFileUsers = root_join("Data", "Users.json")
        with open(dataFileUsers, 'r') as file:
            return json.load(file)

    @staticmethod
    def getUserBooks():
        dataFileUserBooks = root_join("Data", "User-Book.json")
        with open(dataFileUserBooks, 'r') as file:
            return json.load(file)

    #Funksion Ekstra per Kaltrinen
    @staticmethod
    def getAllData():
        return {"users": DataFetcher.getUsers(), "items": DataFetcher.getBooks(), "user-items": DataFetcher.getUserBooks()}




