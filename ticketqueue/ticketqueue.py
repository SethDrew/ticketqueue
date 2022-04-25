from ticketqueue import campers
from typing import Mapping

class TicketAssigner():
    def score_camper(self, camper:campers.Camper):
        return camper.get_camp_score()
    def next_ticketee(self, campers:Mapping[int, campers.Camper]):
        camper_list = filter(lambda c: c.has_ticket != True, campers.values())
        sorted_campers = sorted(camper_list, key=self.score_camper, reverse=True)
        first = sorted_campers[0]
        all_top = list(filter(lambda c: c.get_camp_score() == first.get_camp_score(), sorted_campers))
        return all_top

