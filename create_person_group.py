# oka executed

import cognitive_face as CF
from global_variables import personGroupId
import sys
from global_variables import cfKey
from apiKeys import URL


CF.Key.set(cfKey)
CF.BaseUrl.set(URL)
###################################################################
personGroups = CF.person_group.lists()

for personGroup in personGroups:
    if personGroupId == personGroup['personGroupId']:
        print(personGroupId + " already exists.")
        sys.exit()
# when person group id not exists
res = CF.person_group.create(personGroupId)
print(res)
