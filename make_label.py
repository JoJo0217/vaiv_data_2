import json
import jsonlines
data=[]
file_name='./step1/raw_dataset/gamseong/random_gam_300.jsonl'
save_name=file_name
label='gamseong_'
with open(file_name, "r", encoding="utf-8") as file:
    for line in file:
        data.append( json.loads(line))
idx=1
for one in data:
    one['instruction']=one['prompt']
    del one['prompt']
    one['id']=label+str(idx)
    idx+=1

with jsonlines.open(save_name, mode='w') as writer:
    for one_data in data:
        writer.write(one_data)