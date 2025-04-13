from fastapi import FastAPI
from fastapi.responses import FileResponse
import sqlite3

app = FastAPI()

@app.get("/")
def home():
    return FileResponse("index.html")

@app.get("/subs")
def get_subs():
    conn = sqlite3.connect('subs.db')
    c = conn.cursor()
    c.execute("SELECT name, link, expiry FROM subscriptions")
    subs = [{"name": row[0], "link": row[1], "expiry": row[2]} for row in c.fetchall()]
    conn.close()
    return subs