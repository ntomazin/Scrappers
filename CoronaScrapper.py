#!/home/piki/PycharmProjects/Scrappers/venv/bin/python3

import requests
from bs4 import BeautifulSoup
from configparser import ConfigParser
import re
import sys
import subprocess

def sendmessage(message):
    subprocess.Popen([f"notify-send", message])
    return


config = ConfigParser()
config.read("config.ini")

def main():
    countries = config["countries"]["country"].split(", ")
    if len(sys.argv) > 1:
        countries.extend(sys.argv[1:])

    URL = 'https://www.worldometers.info/coronavirus/'
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')

    results = soup.find(id='main_table_countries_today')
    results = results.prettify()
    output = ""
    for country in countries:
        x = re.search(country.lower(), results.lower())
        country_text = results[x.start():x.start()+500]
        number_of_new_cases = re.search("\+[0-9]+,*[0-9]*", country_text)
        if number_of_new_cases is not None:
            print(f"{country} -> {number_of_new_cases.group()}")
            output += f"{country} -> {number_of_new_cases.group()}\n"


    sendmessage(f"CORONA\n{output}")

if __name__ == "__main__":
    main()
