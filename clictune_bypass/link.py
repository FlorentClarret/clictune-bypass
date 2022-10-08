import re
from typing import Optional
from urllib import parse

import requests
from bs4 import BeautifulSoup

LINK_TEXT_PATTERN = re.compile("Click here to access the link")


def get_url(url: str) -> Optional[str]:
    response = requests.get(url, allow_redirects=False, timeout=20)
    response.raise_for_status()

    soup_response = BeautifulSoup(response.content, "html.parser")
    tag = soup_response.select("td span noscript a", text=LINK_TEXT_PATTERN)

    if tag:
        search = re.search("url=(.*)&id", tag[0].attrs["href"])

        if search and search.lastindex == 1:
            return parse.unquote(search.group(1))

    return None
