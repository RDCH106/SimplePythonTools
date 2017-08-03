# -*- coding: utf-8 -*-

import os
import sys
import platform

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
        except ValueError:
            print("Introduced value is not a number")

    return option_selected


def pressKey():
    if (sys.version_info > (3, 0)):
        input("\n\nPress Enter to continue . . .")
    else:
        raw_input("\n\nPress Enter to continue . . .")

def countLines(file):
    count = 0
    try:
        count = sum(1 for line in open(file))
    except IOError:
        print("File Not Found!")
    return count

if os.name == 'nt' and platform.release() == '10' and platform.version() >= '10.0.14393':
    # Fix ANSI color in Windows 10 version 10.0.14393 (Windows Anniversary Update)
    import ctypes
    kernel32 = ctypes.windll.kernel32
    kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
