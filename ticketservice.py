'''
This script defines the ticket service class that does all the required functions of
a movie ticket system
'''
import sqlite3


class TicketService:
    def __init__(self, cursor):
        self.db = cursor
        return

    # Get movie list
    def get_movie_list(self):
        return self.db.execute("SELECT * FROM movie").fetchall()

    # Book ticket
    def book_ticket(self, show_id, username,  no_of_tickets):
        return self.db.execute("INSERT INTO ticket (showid, username, seats) VALUES ('{}', '{}', '{}')".format(
            show_id, username))

    # Show ticket by id
    def show_ticket_by_id(self, ticket_id):
        data = self.db.execute(
            "SELECT m.name, s.name, t.username, t.seats FROM movie m, show s, ticket t WHERE t.ticketid = {} and t.showid = s.showid and s.movieid = m.movieid".format(ticket_id))
        return data.fetchall()

    # Cancel ticket by id
    def cancel_ticket(self, ticket_id):
        return self.db.execute(
            "DELETE FROM ticket where ticketid = {}".format(ticket_id))

    # Cancel all tickets
    def cancel_all_tickets(self):
        return self.db.execute("DELETE FROM ticket")
