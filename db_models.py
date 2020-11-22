from models import *

db.connect()
# default safe, create if not exists
tables = [Student]
db.create_tables(tables)

####################################################################################

# student = Student.create(fullName="Chester", personGuid=str(uuid.uuid4()))
# student.save()


####################################################################################

for i in Student.select():
    print(f"{i.id} {i.fullName} {i.personGuid}")
    
####################################################################################

db.close()