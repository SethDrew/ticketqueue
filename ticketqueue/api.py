

class Ticketing():
    # todo:: consider other ways of injecting these that follow dependency injection principles.
    # At the moment, dependency inversion is not followed, in the sense that the API depends on classes in the module.
    def __init__(self, ticket_manager, campers):
        self.ticket_manager = ticket_manager
        self.campers = campers

    def campers(self):
        return self.campers

    def next_ticketee(self):
        return self.ticket_manager.next_ticketee(self.campers)




