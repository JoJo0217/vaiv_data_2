import json
import jsonlines
data=[]
file_name='./step2_conf_after_filter.jsonl'
save_name='step2_conf_after_filter_del.jsonl'
with open(file_name, "r", encoding="utf-8") as file:
    for line in file:
        data.append( json.loads(line))
idx=1

result=[]
for one in data:
    if ('modified' in  one)  and (one['modified']=='deleted'):
        continue
    else:
        result.append(one)

with jsonlines.open(save_name, mode='w') as writer:
    for one_data in result:
        writer.write(one_data)