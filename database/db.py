import sqlite3


class DB:
    def __init__(self):
        self.conn = sqlite3.connect('bot.db')
        self.cur = self.conn.cursor()

    def init_db(self):
        self.cur.execute('''CREATE TABLE IF NOT EXISTS posts(
            id INT PRIMARY KEY AUTOINCREMENT,
            group_id TEXT,
            post_hash TEXT
        )''')
        self.conn.commit()

    def find_post(self, group_id: str, post_hash: str):
        self.cur.execute(
            f"SELECT DISTINCT post_hash FROM posts WHERE group_id='{group_id}' AND post_hash='{post_hash}'")

        is_post_exists = self.cur.fetchone()

        if is_post_exists:
            return is_post_exists[0]
        return None

    def add_post(self, group_id: str, post_hash: str):
        self.cur.execute(
            f"INSERT INTO posts(group_id, post_hash) VALUES ('{group_id}','{post_hash}')")
        self.conn.commit()


db = DB()
