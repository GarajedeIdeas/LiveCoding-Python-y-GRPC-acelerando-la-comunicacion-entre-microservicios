import sys
from pymongo import MongoClient

class MongodbRepository():
    __user = ''
    __pwd = ''
    __host = ''
    connection = None

    def __init__(self, user, pwd, host):
        self.__user = user
        self.__pwd = pwd
        self.__host = host

    def __open_connection(self, entity_name) -> None:
        client = MongoClient(
            host = self.__host,
            serverSelectionTimeoutMS = 3000,
            username=self.__user,
            password=self.__pwd,

        )
        self.connection = client["dev"][entity_name]
        print("mongodb connection opened")
    
    def __close_connection(self) -> None:
        #self.connection.close()
        print("close mongodb connection")

    def insert_one(self, data, entity_name):
        try:
            self.__open_connection(entity_name)
            result = self.connection.insert_one(data)
            return result
        except Exception as exception:
            raise Exception('Error reading data: ' + str(exception))
        finally:
            self.__close_connection()

    def insert_many(self, list, entity_name):
        try:
            self.__open_connection(entity_name)
            result = self.connection.insert_many(list)
            return result
        except Exception as exception:
            raise Exception('Error reading data: ' + str(exception))
        finally:
            self.__close_connection()