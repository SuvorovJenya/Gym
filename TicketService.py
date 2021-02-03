# -*- coding: utf8 -*-
import sqlite3
import datetime


class TicketService:
    def __init__(self, db):
        self.db = db
        self.cur = self.db.cursor()
        self.__table_creation()
        self.today = datetime.datetime.today()

    def __table_creation(self):
        self.cur.execute("""CREATE TABLE IF NOT EXISTS ticket_table(id INTEGER PRIMARY KEY, client_id INTEGER,
        cost INTEGER, date_purchases TEXT, date_end TEXT )""")

    def create(self, client_id, cost, date_purchases, date_end):
        self.cur.execute("INSERT INTO ticket_table(client_id, cost, date_purchases, date_end) VALUES (?,?,?,?)",
                         (client_id, cost, date_purchases, date_end))
        self.db.commit()

    def find_one(self, client_id):
        self.cur.execute("SELECT * FROM ticket_table where client_id = ? ORDER BY date_end DESC", (client_id,))
        return self.cur.fetchone()


