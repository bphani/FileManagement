import datetime
import re


b = str(datetime.datetime.now())

result = re.sub("[^0-9]",'_',b)
print(result)