from pony.orm import *


db = Database()


class ForumData(db.Entity):
    count = Required(int)
    date = Required(str)

show(ForumData)