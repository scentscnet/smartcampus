import sqlite3
conn = sqlite3.connect('subject.db')
conn.text_factory = str