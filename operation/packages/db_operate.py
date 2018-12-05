import sqlite3
import time

from .ope import Operater

conn = sqlite3.connect('zaiko.sqlite3')

curs = conn.cursor()

class DB(object):
    def create_table():
        # データベースのテーブル作成
        # 商品のテーブルを作成
        curs.execute('''
                     CREATE TABLE IF NOT EXISTS products(
                     id INTEGER PRIMARY KEY AUTOINCREMENT,
                     name VARCHAR(300) NOT NULL,
                     price INT NOT NULL,
                     left INT NOT NULL
                     );''')
        # commit()で上記のsql文を実行
        conn.commit()


    def add_products():
        while True:
            a = Operater.add_product()
            if a == 'see':
                try:
                    curs.execute('SELECT id, name FROM products;')

                    for i in curs.fetchall():
                        print(i)
                except sqlite3.OperationalError:
                    Operater.say_something(
                    '製品が見つかりませんでした。もう一度やり直してください。')
                    time.sleep(2)
                    continue

            elif a[0] == 'sum':
                num = a[1]
                num = int(num)
                try:
                    curs.execute('''UPDATE products SET left = left + {}
                    WHERE id = {};'''.format(num, int(a[2])))
                    conn.commit()
                except ValueError:
                    Operater.say_something(
                    'エラーが発生しました。\n',
                    '入力したものが半角数字かどうかお確かめの上、もう一度やり直してください')
                    time.sleep(2)
                    continue
            else:
                curs.execute(
                'INSERT INTO products (name, price, left) VALUES (?, ?, ?)'
                , (a[0], a[1], a[2])
                )

                conn.commit()

            fin = Operater.ask_continue()
            if fin is False:
                break


    def delete_product():
        a = Operater.delete()
        check = curs.execute('SELECT name FROM products WHERE id = {}'.format(a))
        isok = Operater.ask_ok(check)
        if isok is True:
            curs.execute('DELETE FROM products WHERE id = {}'.format(a))
        else:
            pass


    def show_all():
        curs.execute('SELECT * FROM products')
        for row in curs.fetchall():
            print(row)
