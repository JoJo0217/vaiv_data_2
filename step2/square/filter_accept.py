import json
import jsonlines

data=[]
result=[]
file_name='response_train.json'
save_name=file_name+'l'
with open(file_name, "r", encoding="utf-8") as file:
        data=json.load(file)

for idx in range(len(data)):
    if data[idx]['acceptable?']==1:
        result.append(data[idx])


with jsonlines.open(save_name, mode='w') as writer:
    for one_data in result:
        writer.write(one_data)