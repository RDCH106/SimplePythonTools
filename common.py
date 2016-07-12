# -*- coding: utf-8 -*-

import os
import sys

def cleanScreen():
    if os.name == 'nt':
        os.system('cls')  # on windows
    else:
        os.system('clear')  # on linux / os x

def askFor(request, nOptions):
    while True:
        try:
            option_selected = int(input(request))
            # Check if input is in range
            if option_selected in range(1, nOptions) or option_selected == 0 or option_selected == -1:
                break
            else:
                print("Out of range. Try again")
        except:
            print("Introduced value is not a number")

    return option_selected


def pressKey():
    if (sys.version_info > (3, 0)):
        wait = input("\n\nPress any key to continue . . .")
    else:
        wait = raw_input("\n\nPress any key to continue . . .")

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'