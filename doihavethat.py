#! /usr/bin/python3

import sys, gspread
from proxyIsOwned import proxyIsOwned

def main(argv):
    sa = gspread.service_account(filename="sa-doihavethat.json")
    sh = sa.open("TCG Inventory")

    mtg = sh.worksheet("MTG")

    proxyIsOwned()

if __name__ == "__main__":
   main(sys.argv[1:])
