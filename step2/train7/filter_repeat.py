from collections import Counter
import re

import json
import jsonlines
from langdetect import detect
from tqdm import tqdm

result=[]
with open('lang_filter_dpo.jsonl', "r", encoding="utf-8") as file:
    for line in file:
        result.append( json.loads(line))
        

def is_most_common_word_over_threshold(text, threshold):
    words = re.findall(r'\b\w+\b', text)
    word_counts = Counter(words)
    most_common_word, most_common_count = word_counts.most_common(1)[0]
    return most_common_count > threshold

#text = "Hello hello Hello. I'm a string with repeated words words words!"
#print(is_most_common_word_over_threshold(text, 2))
filtered_texts=[]
lang=['en','ko']
for one_data in tqdm(result, desc="Processing data"):
    try:
        if(not is_most_common_word_over_threshold(one_data['prompt'], 25) and not is_most_common_word_over_threshold(one_data['chosen'], 25)):
            filtered_texts.append(one_data)
        else:
            print(one_data)
    except:
        print(one_data)

with jsonlines.open("repeat_filter_dpo.jsonl", mode='w') as writer:
    for one_data in filtered_texts:
        writer.write(one_data)