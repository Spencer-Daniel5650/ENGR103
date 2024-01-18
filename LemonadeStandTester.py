# Author: Daniel Spencer
# GitHub Username: Spencer-Daniel5650
# Date: 1/17/2024
# Description: This module tests lemonadestand file

from LemonadeStand import MenuItem, SalesForDay, LemonadeStand, InvalidSalesItemError


class TestLemonadeStand(unittest.TestCase):

    def setUp(self):
        self.stand = LemonadeStand("Test Stand")
        self.lemonade = MenuItem("Lemonade", 0.5, 1.5)
        self.cookies = MenuItem("Cookies", 0.2, 1.0)
        self.stand.add_menu_item(self.lemonade)
        self
