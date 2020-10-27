# https://docs.python.org/3/library/xml.etree.elementtree.html
import xml.etree

# https://docs.python.org/3/library/argparse.html
import argparse

# https://docs.python.org/3/library/csv.html
import csv

# https://docs.python.org/3/library/json.html
import json

# https://dateutil.readthedocs.io/en/2.8.1/
import dateutil.parser

# https://pypi.org/project/html5lib/
import html5lib

# https://requests.readthedocs.io/en/master/
import requests

# https://www.tutorialspoint.com/matplotlib/matplotlib_bar_plot.htm
import numpy as np
import matplotlib.pyplot as plt

from datetime import date

from requests import get
from json import dumps


ENDPOINT = "https://api.coronavirus.data.gov.uk/v1/data"
AREA_TYPE = "utla"
AREA_NAME = "sheffield"

filters = [
    f"areaType={ AREA_TYPE }",
    f"areaName={ AREA_NAME }"
]

structure = {
    "date": "2020-10-11",
    "cases": {
        "daily": "newCasesByPublishDate",
        "cumulative": "cumCasesByPublishDate"
    }
}

api_params = {
    "filters": str.join(";", filters),
    "structure": dumps(structure, separators=(",", ":")),
    "latestBy": "newCasesByPublishDate"
}


response = get(ENDPOINT, params=api_params, timeout=10)

if response.status_code >= 400:
    raise RuntimeError(f'Request failed: { response.text }')

#print(response.url)
print(response.json())
