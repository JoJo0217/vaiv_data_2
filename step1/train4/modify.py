import json
import jsonlines
data=[]
file_name='added_hatespeech.jsonl'
save_name=file_name

with open(file_name, "r", encoding="utf-8") as file:
    for line in file:
        data.append( json.loads(line))

for i in data:
    if 'id'in i:
        i['id']="hatespeech"
    if 'origin_text' in i:
        i['instruction']=i['origin_text']
        del i['origin_text']
    if 'types' in i:
        i['output']=i['types']
        del i['types']

with jsonlines.open(save_name, mode='w') as writer:
    for one_data in data:
        writer.write(one_data)