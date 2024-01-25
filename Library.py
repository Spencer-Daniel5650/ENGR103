# Author: Daniel Spencer
# GitHub Username: Spencer-Daniel5650
# Date: 1/23/2024
# Description: library system simulation with item management, patron interaction, and fines.

class LibraryItem:
    """
    Represents a library item that a patron can check out from a library.
    """

    def __init__(self, library_item_id, title):
        """
        Initialize a new LibraryItem.
        :param library_item_id: Unique identifier for a LibraryItem
        :param title: Title of the LibraryItem
        """
        self._library_item_id = library_item_id
        self._title = title
        self._location = "ON_SHELF"
        self._checked_out_by = None
        self._requested_by = None
        self._date_checked_out = None

    def get_location(self):
        """
        Return the location of the LibraryItem.
        """
        return self._location

    def set_location(self, location):
        """
        Set the location of the LibraryItem.
        :param location: New location of the LibraryItem
        """
        self._location = location

    def get_library_item_id(self):
        """
        Return the library item ID.
        """
        return self._library_item_id

    def get_title(self):
        """
        Return the title of the LibraryItem.
        """
        return self._title

    def get_checked_out_by(self):
        """
        Return the Patron who has the LibraryItem checked out.
        """
        return self._checked_out_by

    def set_checked_out_by(self, patron):
        """
        Set the Patron who has the LibraryItem checked out.
        :param patron: Patron who checked out the LibraryItem
        """
        self._checked_out_by = patron

    def get_requested_by(self):
        """
        Return the Patron who has requested the LibraryItem.
        """
        return self._requested_by

    def set_requested_by(self, patron):
        """
        Set the Patron who has requested the LibraryItem.
        :param patron: Patron who requested the LibraryItem
        """
        self._requested_by = patron

    def get_date_checked_out(self):
        """
        Return the date the LibraryItem was checked out.
        """
        return self._date_checked_out

    def set_date_checked_out(self, date):
        """
        Set the date the LibraryItem was checked out.
        :param date: Date the LibraryItem was checked out
        """
        self._date_checked_out = date


class Book(LibraryItem):
    """
    Represents a book in the library which is a type of LibraryItem.
    """

    def __init__(self, library_item_id, title, author):
        """
        Initialize a new Book.
        :param library_item_id: Unique identifier for the Book
        :param title: Title of the Book
        :param author: Author of the Book
        """
        super().__init__(library_item_id, title)
        self._author = author

    def get_author(self):
        """
        Return the author of the Book.
        """
        return self._author

    def get_check_out_length(self):
        """
        Return the number of days the Book can be checked out for.
        """
        return 21


class Album(LibraryItem):
    """
    Represents an album in the library which is a type of LibraryItem.
    """

    def __init__(self, library_item_id, title, artist):
        """
        Initialize a new Album.
        :param library_item_id: Unique identifier for the Album
        :param title: Title of the Album
        :param artist: Artist of the Album
        """
        super().__init__(library_item_id, title)
        self._artist = artist

    def get_artist(self):
        """
        Return the artist of the Album.
        """
        return self._artist

    def get_check_out_length(self):
        """
        Return the number of days the Album can be checked out for.
        """
        return 14


class Movie(LibraryItem):
    """
    Represents a movie in the library which is a type of LibraryItem.
    """

    def __init__(self, library_item_id, title, director):
        """
        Initialize a new Movie.
        :param library_item_id: Unique identifier for the Movie
        :param title: Title of the Movie
        :param director: Director of the Movie
        """
        super().__init__(library_item_id, title)
        self._director = director

    def get_director(self):
        """
        Return the director of the Movie.
        """
        return self._director

    def get_check_out_length(self):
        """
        Return the number of days the Movie can be checked out for.
        """
        return 7


class Patron:
    """
    Represents a patron of the library.
    """

    def __init__(self, patron_id, name):
        """
        Initialize a new Patron.
        :param patron_id: Unique identifier for the Patron
        :param name: Name of the Patron
        """
        self._patron_id = patron_id
        self._name = name
        self._checked_out_items = []
        self._fine_amount = 0

    def get_fine_amount(self):
        """
        Return the fine amount owed by the Patron.
        """
        return self._fine_amount

    def add_library_item(self, item):
        """
        Add a LibraryItem to the list of items checked out by the Patron.
        :param item: LibraryItem to add
        """
        self._checked_out_items.append(item)

    def remove_library_item(self, item):
        """
        Remove a LibraryItem from the list of items checked out by the Patron.
        :param item: LibraryItem to remove
        """
        self._checked_out_items.remove(item)

    def amend_fine(self, amount):
        """
        Amend the fine amount for the Patron.
        :param amount: Amount to amend the fine by
        """
        self._fine_amount += amount

    def get_patron_id(self):
        """
        Return the patron ID.
        """
        return self._patron_id

    def get_checked_out_items(self):
        """
        Return the list of items checked out by the Patron.
        """
        return self._checked_out_items


class Library:
    """
    Represents a library that contains various library items and is used by various patrons.
    """

    def __init__(self):
        """
        Initialize a new Library.
        """
        self._holdings = []
        self._members = []
        self._current_date = 0

    def add_library_item(self, item):
        """
        Add a LibraryItem to the library's holdings.
        :param item: LibraryItem to add
        """
        self._holdings.append(item)

    def add_patron(self, patron):
        """
        Add a Patron to the library's members.
        :param patron: Patron to add
        """
        self._members.append(patron)

    def lookup_library_item_from_id(self, item_id):
        """
        Lookup a LibraryItem by its ID.
        :param item_id: ID of the LibraryItem
        :return: LibraryItem if found, else None
        """
        for item in self._holdings:
            if item.get_library_item_id() == item_id:
                return item
        return None

    def lookup_patron_from_id(self, patron_id):
        """
        Lookup a Patron by their ID.
        :param patron_id: ID of the Patron
        :return: Patron if found, else None
        """
        for patron in self._members:
            if patron.get_patron_id() == patron_id:
                return patron
        return None

    def check_out_library_item(self, patron_id, library_item_id):
        """
        Check out a LibraryItem for a Patron.
        :param patron_id: ID of the Patron
        :param library_item_id: ID of the LibraryItem
        :return: Status message of the checkout operation
        """
        patron = self.lookup_patron_from_id(patron_id)
        if not patron:
            return "patron not found"

        library_item = self.lookup_library_item_from_id(library_item_id)
        if not library_item:
            return "item not found"

        if library_item.get_location() == "CHECKED_OUT":
            return "item already checked out"

        if library_item.get_requested_by() is not None and library_item.get_requested_by() != patron:
            return "item on hold by other patron"

        library_item.set_checked_out_by(patron)
        library_item.set_date_checked_out(self._current_date)
        library_item.set_location("CHECKED_OUT")
        if library_item.get_requested_by() == patron:
            library_item.set_requested_by(None)
        patron.add_library_item(library_item)
        return "check out successful"

    def return_library_item(self, library_item_id):
        """
        Return a LibraryItem to the library.
        :param library_item_id: ID of the LibraryItem
        :return: Status message of the return operation
        """
        library_item = self.lookup_library_item_from_id(library_item_id)
        if not library_item:
            return "item not found"

        if library_item.get_location() != "CHECKED_OUT":
            return "item already in library"

        patron = library_item.get_checked_out_by()
        patron.remove_library_item(library_item)
        library_item.set_checked_out_by(None)
        if library_item.get_requested_by():
            library_item.set_location("ON_HOLD_SHELF")
        else:
            library_item.set_location("ON_SHELF")
        return "return successful"

    def request_library_item(self, patron_id, library_item_id):
        """
        Request a LibraryItem by a Patron.
        :param patron_id: ID of the Patron
        :param library_item_id: ID of the LibraryItem
        :return: Status message of the request operation
        """
        patron = self.lookup_patron_from_id(patron_id)
        if not patron:
            return "patron not found"

        library_item = self.lookup_library_item_from_id(library_item_id)
        if not library_item:
            return "item not found"

        if library_item.get_requested_by() is not None:
            return "item already on hold"

        library_item.set_requested_by(patron)
        if library_item.get_location() == "ON_SHELF":
            library_item.set_location("ON_HOLD_SHELF")
        return "request successful"

    def pay_fine(self, patron_id, amount):
        """
        Pay the fine for a Patron.
        :param patron_id: ID of the Patron
        :param amount: Amount being paid
        :return: Status message of the payment operation
        """
        patron = self.lookup_patron_from_id(patron_id)
        if not patron:
            return "patron not found"

        patron.amend_fine(-amount)
        return "payment successful"

    def increment_current_date(self):
        """
        Increment the current date and update fines for overdue items.
        """
        self._current_date += 1
        for patron in self._members:
            for item in patron.get_checked_out_items():
                if (self._current_date - item.get_date_checked_out()) > item.get_check_out_length():
                    patron.amend_fine(0.10)
