import json
import jsonlines

data=[]
result=[]
file_name='response_train.jsonl'
save_name=file_name
with open(file_name, "r", encoding="utf-8") as file:
    for line in file:
        data.append( json.loads(line))

for idx in range(len(data)):
    if 'question_en' in data[idx]:
        del data[idx]['question_en']
    if 'response_en' in data[idx]:
        del data[idx]['response_en']


with jsonlines.open(save_name, mode='w') as writer:
    for one_data in data:
        writer.write(one_data)