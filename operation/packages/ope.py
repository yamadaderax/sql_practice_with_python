class Operater(object):

    def say_something(word):
        print('---------------------------------------------------------------')
        print()
        print(word)
        print()
        print('---------------------------------------------------------------')
        print()


    def ask_continue():

        Operater.say_something('''作業を続ける場合は「next」\n
        辞める場合は「fin」と入力してください。''')
        con_or_fin = input()
        con_or_fin.lower()
        if con_or_fin == 'fin':
            return False


    def add_product():
        Operater.say_something('''
        追加する商品のIDを半角数字で入力してください。\n
        データベースに登録していない新製品の場合は、「new」と入力してください。\n
        登録済み商品のIDを確認する場合は「see」と入力してください。
        ''')
        name = input('ID or new or see ：')
        if name == 'new':
            Operater.say_something('新規追加する製品の名前を入力してください。')
            new_name = input('製品名：')
            Operater.say_something(str(new_name) + 'の値段を半角数字で入力してください。')
            price = int(input('値段：'))
            Operater.say_something('追加する個数を半角数字で入力してください。')
            add_num = int(input('追加数：'))

            return new_name, price, add_num

        elif name == 'see':
            return 'see'

        else:
            Operater.say_something('追加する個数を半角数字で入力してください')
            add_num = int(input('追加数：'))
            return 'sum', add_num, name


    def delete():
        Operater.say_something('削除する製品のIDを入力してください。')
        a = input('ID : ')
        a = int(a)
        return a

    def ask_ok(arg):
        Operater.say_something('{}\nこの製品の項目をすべて削除します。' +
        '\n一度削除してしまうと、二度と復元できません。よろしいですか？'.format(arg))
        a = input('yes or no : ')
        a.lower()
        if a == 'yes':
            return True
        else:
            return False


    def ask_operate():
        Operater.say_something('行う操作を下記から選び、その番号を半角で入力してください。\n'
                               + '1 : 製品の追加\n'
                               + '2 : 製品の削除\n'
                               + '3 : 製品の一覧表示')
        a = input('操作番号：')
        a = int(a)
        return a
