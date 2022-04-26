from ticketqueue import ticketqueue, data, campers

from ticketqueue.dash import dashboard

from threading import Thread
import time

def make_table():

    aliases = data.get_entities("data/alias.csv")
    scores = data.get_entities("data/scores.csv")
    tickets = data.get_entities("data/tickets.csv")

    people, aliases = campers.create_campers(aliases, scores, tickets)
    ta = ticketqueue.TicketAssigner()


    list_people = list(people.values())

    reverse_aliases = {v : k for k, v in aliases.items()}

    table = [{**p.as_dict(), "name":reverse_aliases[p.id()]} for p in list_people]

    return table

table = make_table()
dashboard.update(table)

def update_table():
    while 1:
        time.sleep(1)
        table = make_table()
        dashboard.update(table)


thread = Thread(target = update_table)
thread.start()

dashboard.start(True)






