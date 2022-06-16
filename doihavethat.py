#! /usr/bin/python3

import gspread
from needToBuy import needToBuy

def main():
    sa = gspread.service_account(filename="sa-doihavethat.json")
    sh = sa.open("TCG Inventory")

    mtg = sh.worksheet("MTG").get_all_values()
    mtg.remove(mtg[0]) # first row is the header

    needToBuy(mtg)

if __name__ == "__main__":
   main()
