import sqlite3

class DBControler():
    def __init__(self, db_file):
        self.conn = None
        self.db_file = db_file
        self.connect(db_file)

    def query(self, table_name):
        result = []
        sql = "select * from %s" % table_name
        c = self.conn.cursor()
        c.execute(sql)

        rs = c.fetchall()

        for r in rs:
            res = {}
            for key in r.keys():
                res[key] = r[key]
            result.append(res)
        return result

    def connect(self, db_file):
        self.conn = sqlite3.connect(self.db_file)
        self.conn.row_factory = sqlite3.Row

    def disconnect(self):
        self.conn.close()
