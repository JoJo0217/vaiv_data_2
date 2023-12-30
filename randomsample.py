import json
import random
import jsonlines
# Load data from train.json
result =[]
#with open("rm2_final.jsonl", "r", encoding="utf-8") as file:
#    for line in file:
#        result.append(json.loads(line))

#with open("./step1/raw_dataset/gamseong/conv_unique.jsonl", "r", encoding="utf-8") as file:
#        result=json.load(file)
with open('./step2/train6/raw/yitingxie.jsonl', "r", encoding="utf-8") as file:
    for line in file:
        result.append( json.loads(line))

data=result
# Randomly extract 100 items
random.seed(42)  # To ensure reproducibility, set the random seed
random_indices = random.sample(range(len(data)), 1600)
extracted_data = [data[i] for i in random_indices]

# Create two separate lists: extracted_data (100 items) and remaining_data (the rest)
remaining_data = [item for i, item in enumerate(data) if i not in random_indices]

# Save the extracted 100 items to a new JSON file
#with open("eval.json", "w", encoding="utf-8") as file:
#    json.dump(extracted_data, file, ensure_ascii=False, indent=4)
with jsonlines.open("filtered_yitingxie.jsonl", mode='w') as writer:
    for one_data in extracted_data:
        writer.write(one_data)
# Save the remaining data to another JSON file
#with open("train.json", "w", encoding="utf-8") as file:
#    json.dump(remaining_data, file, ensure_ascii=False, indent=4)
#with jsonlines.open("gpt_train.jsonl", mode='w') as writer:
#    for one_data in remaining_data:
#        writer.write(one_data)