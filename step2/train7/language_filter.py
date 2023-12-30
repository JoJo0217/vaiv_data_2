import json
import jsonlines
from langdetect import detect
from tqdm import tqdm

result=[]
with open('ko_Ultrafeedback_binarized.jsonl', "r", encoding="utf-8") as file:
    for line in file:
        result.append( json.loads(line))
        

# 텍스트 리스트 예시
#texts = ["Hello world", "안녕하세요", "Votre texte ici", "Hola mundo"]

# 한국어와 영어 텍스트만 유지
filtered_texts=[]
lang=['en','ko']
for one_data in tqdm(result, desc="Processing data"):
    try:
        if((detect(one_data['prompt']) in lang)):
            filtered_texts.append(one_data)
    except:
        print(one_data)
#filtered_texts = [text for text in texts if detect(text) in ['en', 'ko']]
#print(filtered_texts)
with jsonlines.open("lang_filter_dpo.jsonl", mode='w') as writer:
    for one_data in filtered_texts:
        writer.write(one_data)