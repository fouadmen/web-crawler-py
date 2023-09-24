
import sqlite3


class MetaProcessor():
    def __init__(self):
        self.connection = sqlite3.connect("local.db")
        self.init_db()

    def init_db(self):
        cur = self.connection.cursor()
        cur.execute('''CREATE TABLE if not exists sites
               (id INTEGER PRIMARY KEY autoincrement, site text UNIQUE, num_links int, images int, last_fetch text)''')

    def save_meta(self, meta):
        cur = self.connection.cursor()
        self.delete_meta(meta)
        insert_query = '''INSERT INTO 'sites'
                          ('site', 'num_links', 'images', 'last_fetch') 
                          VALUES (?, ?, ?, ?);'''

        metadata = (meta["site"], meta["num_links"],
                    meta["images"], meta["last_fetch"])
        cur.execute(insert_query, metadata)
        self.connection.commit()

    def delete_meta(self, meta):
        cur = self.connection.cursor()
        delete_query = '''
                    delete from sites where site = ? 
                '''
        metadata = (meta["site"],)
        cur.execute(delete_query, metadata)
        self.connection.commit()

    def load_meta(self, url):
        cur = self.connection.cursor()
        select_query = "SELECT site, num_links, images, last_fetch FROM sites WHERE site = ? ;"
        cur.execute(select_query, (url, ))
        d = cur.fetchone()
        if d is None:
            return None

        meta = {}
        meta["site"] = d[0]
        meta["num_links"] = d[1]
        meta["images"] = d[2]
        meta["last_fetch"] = d[3]

        return meta
