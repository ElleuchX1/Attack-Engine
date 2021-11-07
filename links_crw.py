import requests
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup
import concurrent.futures




internal_urls = set()
external_urls = set()


def is_valid(url):

    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)
def get_all_website_links(url):
    urls = set()
    domain_name = urlparse(url).netloc
    soup = BeautifulSoup(requests.get(url).content, "html.parser" )
    for a_tag in soup.findAll("a"):
        href = a_tag.attrs.get("href")
        if href == "" or href is None:
            continue
        href = urljoin(url, href)
        parsed_href = urlparse(href)
        href = parsed_href.scheme + "://" + parsed_href.netloc + parsed_href.path
        if not is_valid(href):
            continue
        if href in internal_urls:
            continue
        if domain_name not in href:
            if href not in external_urls:
                external_urls.add(href)
            continue
        urls.add(href)
        internal_urls.add(href)
    return urls
total_urls_visited = 0

def crawl(url, max_urls=10):
    global total_urls_visited
    total_urls_visited += 1
    links = get_all_website_links(url)
    if total_urls_visited > max_urls:
        return None
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(crawl, links)

def linkcrawl(url , max_urls=10):
	crawl(url , max_urls)
	T=(internal_urls,external_urls)
	return T
