import os
import requests

def get_puzzle(day):
    return requests.get('http://adventofcode.com/day/{}/input'.format(day), cookies=dict(session=os.environ['ADVENT_SESSION'])).text
