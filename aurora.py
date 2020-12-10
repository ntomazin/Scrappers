#!/home/piki/PycharmProjects/Scrapers/venv/bin/python3

import requests
from bs4 import BeautifulSoup
import re
import subprocess

def sendmessage(message):
    subprocess.Popen([f"notify-send", message])
    return

def main():

    URL = 'https://www.auroranotifier.com/aurora-forecast/'
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')

    results = soup.find_all("div", class_="wpb_wrapper")

    x = re.search("<td>[67]+", str(results))
    if x is not None:
        line = x.string[x.start()-85:x.start()+6]
        dayReg = re.search("Jan|Feb|Mar|Apr|Sep|Oct|Nov|Dec", line)
        day = dayReg.string[dayReg.start(): dayReg.start()+6]
        sendmessage(f"MOGUĆA AURORA BOREALIS\nDANA {day}")
    else:
        sendmessage(f"NEMA MOGUCNOSTI ZA AURORU BOREALIS")


if __name__ == "__main__":
    main()
