from operation.packages import db_operate
from operation.packages import ope

def operate_zaiko():
    db_operate.DB.create_table()
    while True:
        a = ope.Operater.ask_operate()
        if a == 1:
            db_operate.DB.add_products()
        elif a == 2:
            db_operate.DB.delete_product()
        elif a == 3:
            db_operate.DB.show_all()

        a = ope.Operater.ask_continue()
        if a is False:
            ope.Operater.say_something('さようなら。See You!')
            break
        else:
            pass
