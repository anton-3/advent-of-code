#!/usr/bin/env python3
from sys import argv
import requests
from datetime import datetime
from dotenv import load_dotenv
from os import getenv
# THIS IMPORT IS PYTHON 3.9+
# because that's when they added timezones in the standard library apparently 💀💀💀
from zoneinfo import ZoneInfo

load_dotenv()
cookie = getenv('ADVENT_COOKIE')

now = datetime.now(ZoneInfo('America/New_York')) # the timezone that advent uses
year = now.year if len(argv) < 2 else argv[1]
day = now.day if len(argv) < 3 else argv[2]

cookies = {'session': cookie}
link = f'https://adventofcode.com/{year}/day/{day}/input'
headers = {'User-Agent': 'angelettianton@gmail.com'}
print(f'getting input for {year} day {day}')
print(f'requesting {link}...')
res = requests.get(link, headers=headers, cookies=cookies)

if res.ok:
    output_filename = f'{day}.txt'
    text = res.text
    num_lines = text.count('\n')
    print(f'writing input to {output_filename} ({num_lines} lines)')
    with open(output_filename, 'w') as f:
        f.write(text)
else:
    print("error, didn\'t work for some reason, here's the output")
    print(res.text)
