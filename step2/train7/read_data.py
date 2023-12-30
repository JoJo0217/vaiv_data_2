import pandas as pd
import json
import jsonlines
df = pd.read_parquet('train-00000-of-00001-dc7eba5173eb6ca1.parquet', engine = 'pyarrow')
data=[]
for idx, row in df.iterrows():
    one_data={}
    one_data['prompt']=row['prompt']
    one_data['chosen']=row['chosen']
    one_data['rejected']=row['rejected']
    data.append(one_data)

save_name='ko_Ultrafeedback_binarized.jsonl'
with jsonlines.open(save_name, mode='w') as writer:
    for one_data in data:
        writer.write(one_data)