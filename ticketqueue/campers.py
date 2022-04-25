from ticketqueue import data

class Camper():
    def __init__(self, camper_id:int):
        self.camper_id = camper_id
        self.camp_scores = {}
        self.has_ticket = None
    def set_camp_score(self, campscore:int, year:int):
        self.camp_scores[year] = campscore
    def set_has_ticket(self, has_ticket:bool):
        self.has_ticket = has_ticket
    def id(self):
        return self.camper_id

    # todo:: add lambda to define custom functions on scores?
    def get_camp_score(self, applicable_years = [2019]):
        applicable_years.sort(reverse = True)
        for year in applicable_years:
            if year in self.camp_scores:
                return self.camp_scores[year]
        return None #todo log

    def as_dict(self):
        return {"id": self.camper_id, "score": self.get_camp_score(), "ticket": self.has_ticket}

    def __str__(self):
        return "Camper [id: {}, scores: {}, has_ticket: {}]".format(self.camper_id, self.camp_scores, self.has_ticket)
    def __repr__(self):
        return "Camper [id: {}, scores: {}, has_ticket: {}]".format(self.camper_id, self.camp_scores, self.has_ticket)

def create_campers(al_in, ppl_in, tix_in):
    aliases = {} #todo support get and query by alias
    for row in al_in: 
        alias = row['alias'].strip()
        if alias in aliases:
            raise Exception("Alias {} added twice to aliases".format(alias))
        aliases[alias] = int(row['id'].strip())


    people = {}
    for row in ppl_in: 
        name = row['name'].strip()
        campscore = int(row['campscore'].strip())
        year = int(row['year'].strip())
        camper_id = aliases[name]
        
        people.setdefault(camper_id, Camper(camper_id)).set_camp_score(campscore, year)
        
    for row in tix_in: 
        name = row['name'].strip()
        has_ticket = bool(int(row['has_ticket'].strip()))
        camper_id = aliases[name]
        camper = people.setdefault(camper_id, Camper(camper_id)).set_has_ticket(has_ticket)

    return people, aliases
