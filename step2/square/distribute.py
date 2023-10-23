import json
import jsonlines
import pandas as pd

data1=[]
result=dict()
category=['ethical','contentious','etc','predictive']
file1='response_train.jsonl'
save_name='distribute.jsonl'
with open(file1, "r", encoding="utf-8") as file:
    for line in file:
        data1.append( json.loads(line))

for cat in category:
    result=[]
    save_name=f'distribute_{cat}.jsonl'
    for idx in range(len(data1)):
        if str(data1[idx]['question_category']) == cat:
            result.append(data1[idx])
    with jsonlines.open(save_name, mode='w') as writer:
        for one_data in result:
            writer.write(one_data)
