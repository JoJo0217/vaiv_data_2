import json
import jsonlines
data=[]
file_name='./step1/train4/train.jsonl'
save_name=file_name

with open(file_name, "r", encoding="utf-8") as file:
    for line in file:
        data.append( json.loads(line))

for i in data:
    if 'prompt' in i:
        i['instruction']=i['prompt']
        del i['prompt']     
    if 'input' not in i:
        i['input']=""
    if 'chosen' in i:
        i['output']=i['chosen']
        del i['chosen']
    if 'rejected' in i:
        del i['rejected']

with jsonlines.open(save_name, mode='w') as writer:
    for one_data in data:
        writer.write(one_data)