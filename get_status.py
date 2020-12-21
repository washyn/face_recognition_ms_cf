import cognitive_face as CF
from global_variables import *

##############################################################################

CF.Key.set(APIKEY1)
CF.BaseUrl.set(URL)
res = CF.person_group.get_status(personGroupId)

print(res)
