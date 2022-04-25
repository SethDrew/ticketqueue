from .context import ticketqueue

from ticketqueue import ticketqueue, data, campers

def test_found_two_ticketees():
    aliases = data.get_entities("tests/data/alias.csv")
    scores = data.get_entities("tests/data/two_ticketees/scores.csv")
    tickets = data.get_entities("tests/data/tickets.csv")

    people, aliases = campers.create_campers(aliases, scores, tickets)
    ta = ticketqueue.TicketAssigner()
    
    ticketees = ta.next_ticketee(people)
    assert len(ticketees) == 2
    ids = [cm.id() for cm in ticketees]
    assert 3 in ids
    assert 9 in ids




