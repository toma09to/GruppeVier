import sqlite3

class Data:
    def __init__(self):
        self.filename = 'data.db'
        self.id = 0

    def getData(self):
        con = sqlite3.connect(self.filename)
        cur = con.cursor()

        cur.execute(f'SELECT * FROM data WHERE id = {self.id}')
        ret = cur.fetchone()

        cur.close()
        con.close()

        return ret

    def txt(self):
        return self.getData()[1]

    def yes(self):
        next_id = self.getData()[2]
        self.id = next_id

    def no(self):
        next_id = self.getData()[3]
        self.id = next_id

    def isQuestion(self):
        return self.getData()[4] == 1
