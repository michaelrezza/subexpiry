import sqlite3
conn = sqlite3.connect('subs.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS subscriptions (id INTEGER PRIMARY KEY, name TEXT, link TEXT, expiry DATE)''')
c.execute("INSERT INTO subscriptions (name, link, expiry) VALUES ('Test Sub', 'https://example.com', DATE('now', '+1 day'))")
conn.commit()
conn.close()