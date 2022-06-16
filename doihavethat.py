#! /usr/bin/python3

import sys, gspread

def main(argv):
    sa = gspread.service_account(filename="sa-doihavethat.json")
    sh = sa.open("TCG Inventory")

    mtg = sh.worksheet("MTG")

if __name__ == "__main__":
   main(sys.argv[1:])
