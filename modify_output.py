import json
import jsonlines

data=[]
file_name='./step1/raw_dataset/KoAlpaca1.1.jsonl'
save_name='./step1/raw_dataset/KoAlpaca1.1_filtered.jsonl'
del_name='id'
with open(file_name, "r", encoding="utf-8") as file:
    for line in file:
        data.append( json.loads(line))

for one in data:
    tmp=one['output'].split('\n\n 추가')
    one['output']=tmp[0].strip()
    

with jsonlines.open(save_name, mode='w') as writer:
    for one_data in data:
        writer.write(one_data)

