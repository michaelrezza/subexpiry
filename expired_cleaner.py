import sqlite3, datetime
conn = sqlite3.connect('subs.db')
c = conn.cursor()
today = datetime.date.today()
c.execute("DELETE FROM subscriptions WHERE expiry < ?", (today,))
conn.commit()
conn.close()