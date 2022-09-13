# Importing the libraries
import MySQLdb as mdb


class Base(object):
    def __init__(self, database):
        self.DB_ACCESS = mdb.connect(host='localhost', user='root', passwd='')
        self.database = database

    def cursor(self):
        cursor = self.DB_ACCESS.cursor()
        return cursor
