import sqlite3


class DB:
    def __init__(self):
        self.conn = sqlite3.connect('bot.db')
        self.cur = self.conn.cursor()

    def init_db(self):
        self.cur.execute('''CREATE TABLE IF NOT EXISTS posts(
            group_id TEXT PRIMARY KEY,
            post_hash TEXT
        )''')
        self.conn.commit()

    def find_post(self, group_id: str, post_hash: str):
        self.cur.execute(
            f"SELECT DISTINCT post_hash FROM posts WHERE group_id='{group_id}' AND post_hash='{post_hash}'")
        return self.cur.fetchone()

    def add_post(self, group_id: str, post_hash: str):
        self.cur.execute(
            f"INSERT INTO posts(group_id, post_hash) VALUES ('{group_id}','{post_hash}')")
        self.conn.commit()


db = DB()
