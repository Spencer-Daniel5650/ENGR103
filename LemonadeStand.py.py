# Author: Daniel Spencer
# GitHub Username: Spencer-Daniel5650
# Date: 1/17/2024
# Description: This module defines classes for managing a lemonade stand.

class InvalidSalesItemError(Exception):
    """Exception raised for errors in the sales item entry."""
    pass


class MenuItem:
    """Represents a menu item for sale at the lemonade stand."""

    def __init__(self, name, wholesale_cost, selling_price):
        """
        Initialize a new MenuItem instance.
        :param name: Name of the item.
        :param wholesale_cost: Cost of the item to the stand.
        :param selling_price: Selling price of the item.
        """
        self._name = name
        self._wholesale_cost = wholesale_cost
        self._selling_price = selling_price

    def get_name(self):
        """Return the name of the item."""
        return self._name

    def get_wholesale_cost(self):
        """Return the wholesale cost of the item."""
        return self._wholesale_cost

    def get_selling_price(self):
        """Return the selling price of the item."""
        return self._selling_price


class SalesForDay:
    """Represents the sales for a particular day at the lemonade stand."""

    def __init__(self, day, sales_dict):
        """
        Initialize a new SalesForDay instance.
        :param day: Number of days the stand has been open.
        :param sales_dict: Dictionary of items sold and their quantities.
        """
        self._day = day
        self._sales_dict = sales_dict

    def get_day(self):
        """Return the day number."""
        return self._day

    def get_sales_dict(self):
        """Return the dictionary of sales for the day."""
        return self._sales_dict


class LemonadeStand:
    """Represents a lemonade stand."""

    def __init__(self, name):
        """
        Initialize a new LemonadeStand instance.
        :param name: Name of the lemonade stand.
        """
        self._name = name
        self._current_day = 0
        self._menu = {}
        self._sales_record = []

    def get_name(self):
        """Return the name of the stand."""
        return self._name

    def add_menu_item(self, menu_item):
        """
        Add a MenuItem object to the stand's menu.
        :param menu_item: MenuItem object to add.
        """
        self._menu[menu_item.get_name()] = menu_item

    def enter_sales_for_today(self, sales_dict):
        """
        Record sales for the current day.
        :param sales_dict: Dictionary of items sold and their quantities.
        """
        for item_name in sales_dict.keys():
            if item_name not in self._menu:
                raise InvalidSalesItemError(f"{item_name} is not in the menu.")

        sales_for_today = SalesForDay(self._current_day, sales_dict)
        self._sales_record.append(sales_for_today)
        self._current_day += 1

    def sales_of_menu_item_for_day(self, day, item_name):
        """
        Return the number of a specific item sold on a specific day.
        :param day: Day number.
        :param item_name: Name of the menu item.
        """
        if day < 0 or day >= len(self._sales_record):
            return 0  # Day is out of range

        sales_dict = self._sales_record[day].get_sales_dict()
        return sales_dict.get(item_name, 0)  # Return 0 if item not found in sales_dict

    def total_sales_for_menu_item(self, item_name):
        """
        Return the total number of a specific item sold over all days.
        :param item_name: Name of the menu item.
        """
        return sum(self.sales_of_menu_item_for_day(day, item_name) for day in range(self._current_day))

    def total_profit_for_menu_item(self, item_name):
        """
        Return the total profit for a specific item sold over all days.
        :param item_name: Name of the menu item.
        """
        if item_name not in self._menu:
            return 0
        total_sales = self.total_sales_for_menu_item(item_name)
        item = self._menu[item_name]
        return total_sales * (item.get_selling_price() - item.get_wholesale_cost())

    def total_profit_for_stand(self):
        """Return the total profit for all items sold over all days."""
        return sum(self.total_profit_for_menu_item(item_name) for item_name in self._menu)


def main():
    """
    Main function to demonstrate the functionality of the LemonadeStand class.
    """
    stand = LemonadeStand("Sunny Lemonade Stand")
    lemonade = MenuItem("Lemonade", 0.5, 1.5)
    cookies = MenuItem("Cookies", 0.2, 1.0)

    stand.add_menu_item(lemonade)
    stand.add_menu_item(cookies)

    sales_for_today = {"Lemonade": 10, "Cookies": 5, "Sandwich": 2}
    try:
        stand.enter_sales_for_today(sales_for_today)
    except InvalidSalesItemError as e:
        print(f"Invalid sales entry: {e}")


if __name__ == "__main__":
    main()
