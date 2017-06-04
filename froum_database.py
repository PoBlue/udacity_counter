from pony.orm import *
from datetime import date


db = Database()
db.bind('sqlite', 'database.sqlite', create_db=True)
sql_debug(True)


class ForumData(db.Entity):
    count = Required(int)
    record_date = Required(date)

db.generate_mapping(create_tables=True)


@db_session
def add_forum_data(_count, _date):
    new_f = ForumData(count=_count, record_date=_date)


@db_session
def update_forum_count(_data, _count):
    _data.count = _count


@db_session
def get_forum_in_date(_date):
    """
    get data in the _date
    """
    datas = select(f for f in ForumData if f.record_date == _date)[:]
    if len(datas) > 0:
        return datas[0]
    else:
        return None


@db_session
def get_forum_data_recently(_date):
    """
    get data around the date
    """
    datas = select(f for f in ForumData if f.record_date <= _date).order_by(ForumData.record_date)[:]
    if len(datas) > 0:
        return datas[0]
    else:
        return None


@db_session
def get_forum_recently():
    datas = select(f for f in ForumData).order_by(ForumData.record_date)[:]
    if len(datas) > 0:
        return datas[0]
    else:
        return None


@db_session
def get_all_forum_data():
    forums = select(f for f in ForumData)
    return forums[:]

# add_forum_data(1, '2010-01-01')
print(get_forum_data_recently(date(2010, 1, 1)))
