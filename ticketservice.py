'''
This script defines the ticket service class that does all the required functions of
a movie ticket system
'''


from sqlite3.dbapi2 import Error


class TicketService:
    def __init__(self, conn):
        self.db = conn.cursor()
        self.conn = conn
        return

    def get_movie_list(self):
        data = self.db.execute("SELECT * FROM movie").fetchall()
        return data

    def get_show_list(self, movie_id):
        data = self.db.execute(
            "SELECT * FROM show where movieid = {}".format(movie_id)).fetchall()
        return data

    def book_ticket(self, show_id, username,  no_of_tickets):
        try:
            self.db.execute("INSERT INTO ticket (showid, username, seats) VALUES ({}, '{}', {})".format(
                show_id, username, no_of_tickets))
            self.conn.commit()
            return self.db.lastrowid
        except:
            return None

    def get_ticket_by_id(self, ticket_id):
        try:
            data = self.db.execute(
                "SELECT m.name, s.name, t.username, t.seats FROM movie m, show s, ticket t WHERE t.ticketid = {} and t.showid = s.showid and s.movieid = m.movieid".format(ticket_id))
            return data.fetchall()
        except:
            print('No ticket fund with given ID')
            return []

    def cancel_ticket(self, ticket_id):
        try:
            self.db.execute(
                "DELETE FROM ticket where ticketid = {}".format(ticket_id))
            self.conn.commit()

        except:
            print("No ticket found with the given ID")

    def cancel_all_tickets(self):
        self.db.execute("DELETE FROM ticket")
        self.conn.commit()
        return
