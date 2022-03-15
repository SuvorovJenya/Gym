# -*- coding: utf8 -*-
import sqlite3


class ClientService:
    def __init__(self, db):
        self.db = db
        self.cur = self.db.cursor()
        self.__table_creation()

    def __table_creation(self):
        self.cur.execute("""CREATE TABLE IF NOT EXISTS client_table
        (id INTEGER PRIMARY KEY, name TEXT, last_name TEXT)""")

    def create(self, name, last_name):
        self.cur.execute("INSERT INTO client_table(name, last_name) VALUES (?, ?)", (name, last_name))
        self.db.commit()
        return {'id': self.cur.lastrowid}

    def find_one(self, name, last_name):
        self.cur.execute("SELECT * FROM client_table where name = ? and last_name = ?", (name, last_name))
        return self.cur.fetchone()




