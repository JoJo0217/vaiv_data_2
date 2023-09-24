import json
import jsonlines
data=[]
file_name='./step1/train/train.jsonl'
save_name=file_name

with open(file_name, "r", encoding="utf-8") as file:
    for line in file:
        data.append( json.loads(line))

result=[]
for i in data:
    if 'category' in i:
        del i['category']     


with jsonlines.open(save_name, mode='w') as writer:
    for one_data in result:
        writer.write(one_data)