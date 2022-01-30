from py_menu import Menu
from ticketservice import TicketService
from seed import getDB

# Database connection
cursor = getDB()
# Create ticket service
ts = TicketService(cursor)
# Create the menus
main_menu = Menu(header="Booking Kiosk")

def book_movie_menu(show_id):
    try:
        seats = int(input('Enter the numer of seats you want to book: '))
        name = input('Enter your name: ')
        id = ts.book_ticket(show_id, name, seats)
        if id is None:
            print('Something went wrong')
            return 0  # Exit progrm due to error
        print('Your ticket with id: {}, has been booked'.format(id))
        # Return to main menu
        return 1
    except:
        print("Invalid option")
        book_movie_menu(show_id)


def get_show_timings(movie_id):
    show_menu = Menu(header="Choose a show")
    show_list = ts.get_show_list(movie_id)
    for show in show_list:
        show_menu.add_option(show[-1], lambda show_id=show[0]: book_movie_menu(show_id), False)
    show_menu.mainloop()


def get_movie_list():
    movie_menu = Menu(header="Choose a movie")
    movie_list = ts.get_movie_list()
    for movie in movie_list:
        movie_menu.add_option(
            movie[1], lambda movie_id=movie[0]: get_show_timings(movie_id), False)
    movie_menu.mainloop()


def get_ticket_info():
    try:
        ticket_id = int(input('Please enter the ticket id: '))
        data = ts.get_ticket_by_id(ticket_id)
        if len(data) <= 0:
            print('No ticket with ID {} was found'.format(ticket_id))
            return 1
        for d in data:
            print('Ticket ID: {}\nMovie: {}\nShow: {}\nCustomer: {}\nSeats: {}\n'.format(
                ticket_id, d[0], d[1], d[2], d[3]))
    except:
        print("Invalid option")
    # Return to main menu
    return 1


def cancel_ticket():
    try:
        ticket_id = int(input('Please enter the ticket id: '))
        ts.cancel_ticket(ticket_id)
    except:
        print("Invalid option")
        cancel_ticket()
    # Return to main menu
    return 1


def cancel_all_tickets():
    ts.cancel_all_tickets()
    print("All tickets were canceled.")
    # Return to main menu
    return 1


# Add main menu options
main_menu.add_option("Book a movie", lambda: get_movie_list(), False)
main_menu.add_option("Get ticket by ID", lambda: get_ticket_info(), False)
main_menu.add_option("Cancel a ticket by ID", lambda: cancel_ticket(), False)
main_menu.add_option("Cancel all tickets", lambda: cancel_all_tickets(), False)

# Start the menu service
main_menu.mainloop()
