from webScrapping import getContent
import json

with open('News_Category_Dataset_v2.json', 'r') as handle:
    data = [json.loads(line) for line in handle]

import random

r = random.randint(0,len(data))
getContent(data[r]['link'])

print()
print(data[r]['headline'])

getContent('https://www.huffingtonpost.com/entry/texas-amanda-painter-mass-shooting_us_5b081ab4e4b0802d69caad89')
