#! /usr/bin/python3

import gspread

sa = gspread.service_account(filename="sa-doihavethat.json")
sh = sa.open("TCG Inventory")

mtg = sh.worksheet("MTG")
