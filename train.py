##############################################################################
import cognitive_face as CF
from global_variables import *


CF.Key.set(cfKey)
CF.BaseUrl.set(URL)

res = CF.person_group.train(personGroupId)
print(res)