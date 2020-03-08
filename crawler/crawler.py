import json
import os
from concurrent.futures import ThreadPoolExecutor

import urllib3
from bs4 import BeautifulSoup

BASE_URL = "https://www.goodreads.com/quotes/tag/drinking"
PAGE_COUNT = 21
PAGE_PARAMS = [""] + [f"?page={x}" for x in range(2, PAGE_COUNT + 1)]
OUTPUT_FILE = "quotes.json"

http = urllib3.PoolManager()


def _get_quote(stripped_strings):
    quote_parts = []
    for x in stripped_strings:
        quote_parts.append(x)
        if "”" in x:
            break
    return "\n".join(quote_parts)


def _query_quotes(page_param):
    _quotes = []
    _authors = []

    query_url = BASE_URL + page_param
    response = http.request("GET", query_url)
    soup = BeautifulSoup(response.data, features="html.parser")

    quotes_blocks = soup.findAll("div", {"class": "quoteText"})
    _quotes += [_get_quote(x.stripped_strings) for x in quotes_blocks]

    author_blocks = soup.findAll("span", {"class": "authorOrTitle"})
    _authors += [next(x.stripped_strings).replace(",", "") for x in author_blocks]

    return list(zip(_quotes, _authors, [query_url] * len(_quotes)))


authored_quotes = []

with ThreadPoolExecutor() as executor:
    authored_quotes = executor.map(_query_quotes, PAGE_PARAMS)

authored_quotes = [
    {"quote": x[0], "author": x[1], "source": x[2]} for x in sum(authored_quotes, [])
]

with open(
    os.path.join(os.path.dirname(os.path.realpath(__file__)), OUTPUT_FILE), "w"
) as output_file:
    json.dump(authored_quotes, output_file, indent=4)
