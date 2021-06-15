from webScrapping import getContent
import json

with open('News_Category_Dataset_v2.json', 'r') as handle:
    data = [json.loads(line) for line in handle]

wordCounter = []

for news in data :
    name = news['category']
    filename = name + ".txt"

    text,wordCount = getContent(news['link'])

    if wordCount > 0 :
        with open('news/'+filename,"a+",encoding='utf-8') as f:
            f.write(str(text))
            f.write("\n\n")
        
    wordCounter.append(wordCount)

print(wordCounter)