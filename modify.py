import json
import jsonlines
data=[]
file_name='./step1/raw_dataset/conversation/after/5.jsonl'
save_name='./step1/raw_dataset/conversation/after/5_modified.jsonl'

with open(file_name, "r", encoding="utf-8") as file:
    for line in file:
        data.append( json.loads(line))

result=[]
for i in data:
    if 'modified' in i:
        if i['modified']==True:
            result.append(i)
    else:
        result.append(i)            


with jsonlines.open(save_name, mode='w') as writer:
    for one_data in result:
        writer.write(one_data)