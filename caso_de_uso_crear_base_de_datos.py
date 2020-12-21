from models import *

db.connect()

tables = [Student]

db.create_tables(tables)

db.close()
