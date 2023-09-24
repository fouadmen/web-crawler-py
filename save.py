import os
import sys
import requests
import shutil
from meta import MetaProcessor
from datetime import datetime, timezone
from urllib.parse import urlparse
from utils import *


class Save():

    def save_site(self, html, url):
        try:
            self.dir_name = format_dir_name(url)

            if os.path.exists(self.dir_name):
                shutil.rmtree(self.dir_name, ignore_errors=True)

            os.mkdir(self.dir_name)

            with open("./%s/index.html" % (self.dir_name), "w") as fs:
                fs.write(str(html))
                fs.close()
        except OSError as e:
            print("Error while crating file")
            print(e)
            sys.exit()

    def save_assets(self, html, url):
        with open("./%s/index.html" % (self.dir_name), "r") as fs:
            for link in html.find_all('link', href=True):
                try:
                    path = urlparse(link["href"]).path.split("/")
                    directory = "/".join(path[:-1])
                    path = "/".join(path)

                    content = download_file(format_url(url, link["href"]))
                    if content:
                        os.makedirs("./%s%s" %
                                    (self.dir_name, directory), exist_ok=True)
                        with open("./%s%s" % (self.dir_name, path), "wb") as fs:
                            fs.write(content)

                    link["href"] = "./%s%s" % (self.dir_name, path)
                except:
                    continue

            for img in html.find_all('img', src=True):
                try:
                    path = urlparse(img["src"]).path.split("/")
                    directory = "/".join(path[:-1])
                    path = "/".join(path)

                    content = download_file(self.format_url(url, img["src"]))
                    if content:
                        os.makedirs("./%s%s" %
                                    (self.dir_name, directory), exist_ok=True)
                        with open("./%s%s" % (self.dir_name, path), "wb") as fs:
                            fs.write(content)

                    img["img"] = "./%s%s" % (self.dir_name, path)
                except:
                    continue
            fs.close()

        with open("./%s/index.html" % (self.dir_name), "w") as fs:
            fs.write(str(html))
            fs.close()

    def save_meta(self, html, url):
        meta = {}
        meta["site"] = url
        meta["num_links"] = len(html.find_all('a', href=True))
        meta["images"] = len(html.find_all('img', src=True))
        meta["last_fetch"] = datetime.now(
            timezone.utc).strftime("%a %b %d %Y %H:%M UTC")
        mp = MetaProcessor()
        mp.save_meta(meta)
