#!/usr/bin/python3
import sys
from bs4 import BeautifulSoup

filename = sys.argv[1]

with open(filename) as f:
    soup = BeautifulSoup(f, "html.parser")

print(soup.main)