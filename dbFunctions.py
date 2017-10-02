import sqlite3

# Class to open and manage the data base from file
class opendb(object):

    def __init__(self):
        self.connection = sqlite3.connect('stops.db3')
        self.cursor = self.connection.cursor()

    def close(self):
        self.connection.close

# To create a table on the DB
def createTable():

    sql = opendb()
    cursor = sql.cursor

    cursor.execute('''CREATE TABLE IF NOT EXISTS paradas (name text, date real)''')

    sql.close()
    return True

# To insert a Device event data in the DB
def insertEvent(device):
    sql = opendb()

    sql.cursor.execute("INSERT INTO paradas VALUES (?,?)",
                  [device["name"],
                   device["date"]
                   ])

    sql.connection.commit()
    sql.close()
    return True

# To convert database reading into dictionary
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

# To get all events from datatabase into a dictionary list
def getAllEvents():
    sql = opendb()
    con = sql.connection

    con.row_factory = dict_factory
    cur = con.cursor()
    cur.execute("SELECT * FROM paradas")

    return cur.fetchall()

# To get all event from specified devices into a dictonary list
def getAllEventsFrom(deviceName):
    sql = opendb()
    con = sql.connection

    con.row_factory = dict_factory
    cur = con.cursor()

    t = (deviceName,)
    cur.execute("SELECT * FROM paradas WHERE name = ?", t)

    return cur.fetchall()

def getLastFrom(deviceName):
    sql = opendb()
    con = sql.connection

    con.row_factory = dict_factory
    cur = con.cursor()

    t = (deviceName,)
    cur.execute("SELECT MAX(date) as date, name FROM paradas WHERE name = ?", t)

    return cur.fetchall()

def getLast():
    sql = opendb()
    con = sql.connection

    con.row_factory = dict_factory
    cur = con.cursor()

    cur.execute("SELECT name, MAX(date) as date FROM paradas")

    return cur.fetchall()


def getLastP():
    sql = opendb()
    con = sql.connection

    con.row_factory = dict_factory
    cur = con.cursor()

    cur.execute("SELECT name, MAX(date) as date FROM paradas GROUP BY name ORDER BY date DESC")

    return cur.fetchall()

