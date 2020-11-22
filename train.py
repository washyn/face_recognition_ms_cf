##############################################################################
import cognitive_face as CF
from global_variables import personGroupId
from global_variables import cfKey
from global_variables import URL


CF.Key.set(cfKey)
CF.BaseUrl.set(URL)

res = CF.person_group.train(personGroupId)
print(res)