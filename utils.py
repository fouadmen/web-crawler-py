from urllib.parse import urlparse
import requests


def format_url(base_url, url):
    res, res_base = urlparse(url), urlparse(base_url)
    if res_base.netloc == res.netloc:
        return None
    if res.netloc == '':
        return base_url + url
    return url


def download_file(file_url):
    if not file_url:
        return None
    res = requests.get(file_url, stream=True)
    if res.status_code == 200:
        return res.content
    return None


def format_dir_name(url):
    res = urlparse(url)
    return "%s.html" % (res.netloc)


def unify_urls(url):
    return url if url[-1] == "/" else url + "/"
