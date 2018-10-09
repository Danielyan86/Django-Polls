import sqlite3
import time

current = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
conn = sqlite3.connect('../Django_polls/db.sqlite3')
c = conn.cursor()
c.execute("INSERT INTO polls_question "
          "(question_text, pub_date) "
          "VALUES ('what is your name','{0}')".format(str(current)))


conn.commit()
