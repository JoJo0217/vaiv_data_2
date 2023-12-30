import json
import jsonlines
load_file="train.jsonl"
save_file="train.jsonl"
# eval.json 파일 로드
with open(load_file, "r", encoding="utf-8") as file:
    #data = json.load(file)
    data = [json.loads(line) for line in file.readlines()]

# "### 질문: "과 "### 답변: "을 prompt에 붙이기
for item in data:
    #item["prompt"] = f"### 질문: {item['prompt']} ### 답변: "
    item['chosen']=item['chosen']+"<|endoftext|>"
    item['rejected']=item['rejected']+"<|endoftext|>"
    if 'id' in item:
        del item['id']
# 수정된 데이터를 새로운 JSON 파일로 저장
#with open(save_file, "w", encoding="utf-8") as file:
#    json.dump(data, file, ensure_ascii=False, indent=4)
with jsonlines.open(save_file, mode='w') as writer:
    for one_data in data:
        writer.write(one_data)