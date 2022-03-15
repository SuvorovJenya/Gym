# -*- coding: utf8 -*-
import sqlite3
import datetime
from enums import TicketType
from ClientService import ClientService
from TicketService import TicketService
from utils import dict_factory


class GymService:
    def __init__(self):
        self.db = sqlite3.connect('gym.db')
        self.db.row_factory = dict_factory
        self.client_service = ClientService(self.db)
        self.ticket_service = TicketService(self.db)
        self.today = datetime.datetime.today()

    def start_work_with_client(self, name, last_name):
        client = self.client_service.find_one(name, last_name)
        if client:
            ticket = self.ticket_service.find_one(client['id'])
            if ticket:
                self.check_date(ticket, client)
        else:
            client = self.client_service.create(name, last_name)
            self.suggest_to_buy_ticket(client)

    def suggest_to_buy_ticket(self, client):
        answer = int(input('Какой абонемент хотите приобрести: дневной(1)/вечерний(2)?\n'))
        if answer == 1:
            ticket_type = TicketType.day
        elif answer == 2:
            ticket_type = TicketType.night
        else:
            return print('Нет такого абонемента')
        cost = ticket_type.value
        date_purchases = self.today.strftime("%m/%d/%Y")
        date_end = (self.today + datetime.timedelta(1 * 365 / 12)).strftime("%m/%d/%Y")
        self.ticket_service.create(client['id'], cost, date_purchases, date_end)

    def check_date(self, ticket, client):
        if ticket['date_end'] < self.today.strftime("%m/%d/%Y"):
            print('У вас закончился абонемент')
            self.suggest_to_buy_ticket(client)
        else:
            print(f"Цена: {ticket['cost']} \n"
                  f"Дата начала: {ticket['date_purchases']} \n"
                  f"Дата окончания: {ticket['date_end']}")













