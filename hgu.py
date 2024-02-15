import sqlite3

con = sqlite3.connect('data.db')
cur = con.cursor()

data = (
    {'id': 0, 'content': '発熱（平熱＋1℃前後以上）等の風邪症状、息苦しさ、強いだるさがある', 'to_yes': 1, 'to_no': 2, 'is_question': 1},
    {'id': 1, 'content': '自宅待機　症状が強い場合は、病院か帰国者・接触者相談センターへ相談', 'to_yes': None, 'to_no': None, 'is_question': 0},
    {'id': 2, 'content': '同居する家族が感染または感染の疑いがある', 'to_yes': 3, 'to_no': 4, 'is_question': 1},
    {'id': 3, 'content': '自宅待機', 'to_yes': None, 'to_no': None, 'is_question': 0},
    {'id': 4, 'content': '発熱や咳など軽い風邪症状がある', 'to_yes': 5, 'to_no': 6, 'is_question': 1},
    {'id': 5, 'content': '自宅待機　症状が4日以上続く場合は、病院か帰国者・接触者相談センターへ相談', 'to_yes': None, 'to_no': None, 'is_question': 0},
    {'id': 6, 'content': 'ストレス症状がある', 'to_yes': 7, 'to_no': 8, 'is_question': 1},
    {'id': 7, 'content': '登校（健康調査票を忘れずに！）　先生に相談しましょう。スクールカウンセラーも利用できます。', 'to_yes': None, 'to_no': None, 'is_question': 0},
    {'id': 8, 'content': '登校（健康調査票を忘れずに！）', 'to_yes': None, 'to_no': None, 'is_question': 0},
)

cur.executemany('INSERT INTO data VALUES(:id, :content, :to_yes, :to_no, :is_question)', data)

con.commit()

cur.close()
con.close()
