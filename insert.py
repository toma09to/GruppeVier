import sqlite3

con = sqlite3.connect('data.db')
cur = con.cursor()

data = (
        {'id': 0, 'content': 'これは質問0です', 'to_yes': 1, 'to_no': 2, 'is_question': 1},
        {'id': 1, 'content': 'これは質問1です', 'to_yes': 3, 'to_no': 4, 'is_question': 1},
        {'id': 2, 'content': 'これは質問2です', 'to_yes': 5, 'to_no': 6, 'is_question': 1},
        {'id': 3, 'content': 'これは質問3です', 'to_yes': 7, 'to_no': 8, 'is_question': 1},
        {'id': 4, 'content': 'これは質問4です', 'to_yes': 9, 'to_no': 10, 'is_question': 1},
        {'id': 5, 'content': 'これは質問5です', 'to_yes': 11, 'to_no': 12, 'is_question': 1},
        {'id': 6, 'content': 'これは質問6です', 'to_yes': 13, 'to_no': 14, 'is_question': 1},
        {'id': 7, 'content': 'これは答え0です', 'to_yes': None, 'to_no': None, 'is_question': 0},
        {'id': 8, 'content': 'これは答え1です', 'to_yes': None, 'to_no': None, 'is_question': 0},
        {'id': 9, 'content': 'これは答え2です', 'to_yes': None, 'to_no': None, 'is_question': 0},
        {'id': 10, 'content': 'これは答え3です',  'to_yes': None, 'to_no': None, 'is_question': 0},
        {'id': 11, 'content': 'これは答え4です',  'to_yes': None, 'to_no': None, 'is_question': 0},
        {'id': 12, 'content': 'これは答え5です',  'to_yes': None, 'to_no': None, 'is_question': 0},
        {'id': 13, 'content': 'これは答え6です',  'to_yes': None, 'to_no': None, 'is_question': 0},
        {'id': 14, 'content': 'これは答え7です',  'to_yes': None, 'to_no': None, 'is_question': 0},
)

cur.executemany('INSERT INTO data VALUES(:id, :content, :to_yes, :to_no, :is_question)', data)

con.commit()

cur.close()
con.close()
