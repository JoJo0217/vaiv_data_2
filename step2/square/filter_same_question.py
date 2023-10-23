import json
import jsonlines

data=[]
result=[]
removed=set()
file_name='response_train.json'
save_name='merged_same.jsonl'
with open(file_name, "r", encoding="utf-8") as file:
        data=json.load(file)

for i in range(len(data)):
    print(i)
    if i not in removed: 
        merged=dict()
        merged['question']=data[i]['question']
        merged["responses"]=[data[i]['response']]
        merged['acceptable?']=[data[i]['acceptable?']]
        merged['category']=[data[i]['category']]
        merged['question_category']=[data[i]['question_category']]
        for j in range(i+1,len(data)):
            if data[i]['question']==data[j]['question']:
                removed.add(j)
                merged["responses"].append(data[j]['response'])
                merged["acceptable?"].append(data[j]['acceptable?'])
                merged["category"].append(data[j]['category'])
                merged["question_category"].append(data[j]['question_category'])
            
        if(len(merged['acceptable?'])>=2):    
            result.append(merged)
            


with jsonlines.open(save_name, mode='w') as writer:
    for one_data in result:
        writer.write(one_data)