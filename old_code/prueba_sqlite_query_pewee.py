from models import *


def getCurrentFakeFaceIdByUserId():
    resultFolderGuid = None
    # db = SqliteDatabase(sqliteDbFileName)
    # db.connect()
    
    student = Student.get_by_id(6)
    
    resultFolderGuid = student
    # for i in students:
    #     if i == idToFind:
    #         resultFolderGuid = i.folderGuid
    # db.close()
    return resultFolderGuid


print(getCurrentFakeFaceIdByUserId())