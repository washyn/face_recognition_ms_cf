import cognitive_face as CF
from global_variables import *

##############################################################################

CF.Key.set(APIKEY1)
CF.BaseUrl.set(URL)
res = CF.person_group.get_status(personGroupId)

# {'status': 'succeeded', 'createdDateTime': '2020-11-22T01:09:26.9118677Z', 'lastActionDateTime': '2020-11-22T01:09:27.2163835Z'}
print(res)
