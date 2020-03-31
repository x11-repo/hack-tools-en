# -*- coding: utf-8 -*-
import os
import string
import sys
from colorama import Fore, Back, Style

#Author-x11repo#
#When copying, please specify me as the Author and do not delete these lines
#!# Update 0.5 Beta #!#

os.system("cls")
os.system("clear")
print(Fore.BLUE+f"╔═════════════════════════════════╗")
print(Fore.BLUE+f"║ {Fore.YELLOW}~-~-~-~-{Style.RESET_ALL}Choose your OS{Fore.YELLOW}-~-~-~-~-~{Fore.BLUE}║"+Style.RESET_ALL)
print(Fore.BLUE+f"║ {Fore.YELLOW}~-~-~-~-~-{Style.RESET_ALL}1. MacOs{Fore.YELLOW}-~-~-~-~-~-~-~{Fore.BLUE}║"+Style.RESET_ALL)
print(Fore.BLUE+f"║ {Fore.YELLOW}~-~-~-~-~-{Style.RESET_ALL}2. Windows 10{Fore.YELLOW}~-~-~-~-~{Fore.BLUE}║"+Style.RESET_ALL)
print(Fore.BLUE+f"║ {Fore.YELLOW}~-~-~-~-~-{Style.RESET_ALL}3. Kali core{Fore.YELLOW}-~-~-~-~-~{Fore.BLUE}║"+Style.RESET_ALL)
print(Fore.BLUE+f"║ {Fore.YELLOW}~-~-~-~-~-{Style.RESET_ALL}4. Android{Fore.YELLOW}-~-~-~-~-~-~{Fore.BLUE}║"+Style.RESET_ALL)
print(Fore.BLUE+f"╚═════════════════════════════════╝")

ososos = input(Fore.YELLOW+f" Enter 1/2/3 or 4: ")
if ososos == "1":
    from core import macos

if ososos == "2":
    from core import windows

if ososos == "3":
    from core import kali

if ososos == "4":
    from core import android

else:
    print(Fore.RED+f"[x] {Style.RESET_ALL}You entered an incorrect value.")