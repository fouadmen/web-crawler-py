import argparse
from fetch_module import Fetch
from meta import MetaProcessor
from save import Save
from utils import *


_fetch = Fetch()
_save = Save()
mp = MetaProcessor()


def fetch_and_save(url):
    _url = unify_urls(url)
    html = _fetch.fetch_url(_url)
    _save.save_site(html, _url)
    _save.save_assets(html, _url)
    _save.save_meta(html, _url)


def fetch_metadata(url):
    url = unify_urls(url)
    metadata = mp.load_meta(url)
    if metadata:
        for k, v in metadata.items():
            print("%s : %s" % (k, v))
    else:
        print("This site does not exist.")


def main():
    parser = argparse.ArgumentParser(
        description="Fetch web pages and save them to disk.")
    parser.add_argument("urls", nargs='+', help="List of URLs to fetch.")
    parser.add_argument("--metadata", action="store_true",
                        help="Print metadata about the fetched URLs.")

    args = parser.parse_args()

    for url in args.urls:
        fetch_and_save(url)
        if args.metadata:
            fetch_metadata(url)


if __name__ == "__main__":
    main()
