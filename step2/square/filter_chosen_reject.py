import json
import jsonlines

data=[]
result=[]
removed=set()
file_name='merged_same.jsonl'
save_name='train_chosen_reject.jsonl'
with open(file_name, "r", encoding="utf-8") as file:
    for line in file:
        data.append( json.loads(line))

with jsonlines.open(save_name, mode='w') as writer:
    for one_data in data:
        if (0 in one_data['acceptable?']) and (1 in one_data['acceptable?']):
            merged=dict()
            merged['prompt']=one_data['question']
            one_idx=[]
            zero_idx=[]
            for idx,one in enumerate(one_data['acceptable?']):
                if one==1:
                    one_idx.append(idx)
                else:
                    zero_idx.append(idx)
            
            for i in one_idx:
                for j in zero_idx:
                    merged['chosen']=one_data['responses'][i]
                    merged['rejected']=one_data['responses'][j]
                    writer.write(merged)

