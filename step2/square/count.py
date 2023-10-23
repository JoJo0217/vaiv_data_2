import json
import jsonlines
import pandas as pd

data1=[]
result=dict()
file1='response_train.jsonl'
save_name='counted_category.jsonl'
with open(file1, "r", encoding="utf-8") as file:
    for line in file:
        data1.append( json.loads(line))

for idx in range(len(data1)):
    if str(data1[idx]['question_category']) not in result:
        result[str(data1[idx]['question_category'])]=1
    else:
        result[str(data1[idx]['question_category'])]+=1

    
    with jsonlines.open(save_name, mode='w') as writer:
            writer.write(result)