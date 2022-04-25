from ticketqueue import ticketqueue, data, campers

from ticketqueue.dash import dashboard

aliases = data.get_entities("data/alias.csv")
scores = data.get_entities("data/scores.csv")
tickets = data.get_entities("data/tickets.csv")

people, aliases = campers.create_campers(aliases, scores, tickets)
ta = ticketqueue.TicketAssigner()


list_people = list(people.values())

reverse_aliases = {v : k for k, v in aliases.items()}

table = [{**p.as_dict(), "name":reverse_aliases[p.id()]} for p in list_people]


dashboard.init(table)
dashboard.start(True)


