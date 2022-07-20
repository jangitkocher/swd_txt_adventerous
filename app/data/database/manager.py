from pymongo import MongoClient


class ObjectName:
    REGISTERED_USER = "registered_user"
    GAME = "game"
    pass


class DataBaseManager:
    def __init__(self, ip_addr: str, port: int):
        self.client = MongoClient(f"mongodb://{ip_addr}:{port}")
        self.db = self.client.textadventure
        pass

    def add_object(self, object_name: ObjectName, data: dict):
        try:
            self.db[object_name].insert_one(data)
        except Exception:
            raise DatabaseException()
        pass

    def get_object(self, object_name: ObjectName, search_param: dict):
        try:
            result = self.db[object_name].find_one(search_param)
            if result is None:
                raise DatabaseException()
            else:
                return result
        except Exception:
            raise DatabaseException()
        pass

    def update_object(self, object_name: ObjectName, search_param: dict, update_function: dict):
        try:
            self.db[object_name].updaet_one(search_param, update_function)
        except Exception:
            raise DatabaseException()
        pass

    def get_all_objects(self, object_name: ObjectName):
        try:
            result = self.db[object_name].find()
            if result is None:
                raise DatabaseException()
            else:
                return result
        except Exception:
            raise DatabaseException()
        pass


class DatabaseException(Exception):
    pass
